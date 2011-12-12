#!/usr/bin/env python
#
# Basic Strategy
# 0) Ignore data except the useful
# 1) Read in all of the segments (and junctions and components)
# 2) Divide all the segments by the junctions
# 3) Calculate the nets from the segments
# 4) Read the part library to figure out pin connectivity [TODO]

from core.design import Design
from core.components import Component, Symbol, Body, Pin
from core.net import Net, NetPoint
from core import shape

from os.path import exists, splitext


class KiCAD:
    """ The KiCAD Format Parser """

    def parse(self, filename, library_filename=None):
        """ Parse a kicad file into a design """

        # Rough'n'dirty parsing, assume nothing useful comes before
        # the description
        circuit = Design()
        segments = set() # each wire segment
        junctions = set() # wire junction point (connects all wires under it)

        if library_filename is None:
            library_filename = splitext(filename)[0] + '-cache.lib'
            if exists(library_filename):
                self.parse_library(library_filename, circuit)

        f = open(filename)

        # Read until the end of the description
        while f.readline().strip() != "$EndDescr":
            pass

        # Now parse wires and components, ignore connections, we get
        # connectivity from wire segments

        line = f.readline()
        while line:
            element = line.split()[0] # whats next on the list
            if element == "Wire": # Wire Segment, coords on 2nd line
                x1,y1,x2,y2 = [int(i) for i in f.readline().split()]
                if not(x1 == x2 and y1 == y2): # ignore zero-length segments
                    segments.add(((x1,y1),(x2,y2)))
            elif element == "Connection": # Store these to apply later
                x,y = [int(i) for i in line.split()[2:4]]
                junctions.add((x,y))
            elif element == "$Comp": # Component Instance
                # name & reference
                prefix,name,reference = f.readline().split()
                assert prefix == 'L'

                # timestamp
                prefix, _ = f.readline().split(None, 1)
                assert prefix == 'U'

                # position
                prefix, compx,compy = f.readline().split()
                assert prefix == 'P'
                compx, compy = int(compx), int(compy)

                # TODO(ajray): ignore all the fields for now, probably
                # could make these annotations

                while f.readline().strip() not in ("$EndComp", ''):
                    pass

            line = f.readline()

        f.close()

        segments = self.divide(segments, junctions)
        circuit.nets = self.calc_nets(segments)

        return circuit


    def parse_library(self, filename, circuit):
        """
        Parse the library file and add the components to the given
        circuit.
        """

        f = open(filename)

        for line in f:
            parts = line.strip().split()
            prefix = parts[0]

            if prefix == 'DEF':
                component = Component(parts[1])
                component.add_attribute('_prefix', parts[2])
                symbol = Symbol()
                component.add_symbol(symbol)
                body = Body()
                symbol.add_body(body)
            elif prefix == 'A': # Arc
                x, y, radius, start, end = [int(i) for i in parts[1:6]]
                # convert tenths of degrees to pi radians
                start = round(start / 1800.0, 1)
                end = round(end / 1800.0, 1)
                body.add_shape(shape.Arc(x, y, start, end, radius))
            elif prefix == 'C': # Circle
                x, y, radius = [int(i) for i in parts[1:4]]
                body.add_shape(shape.Circle(x, y, radius))
            elif prefix == 'P': # Polyline
                num_points = int(parts[1])
                poly = shape.Polygon()
                for i in xrange(num_points):
                    x, y = int(parts[5 + 2 * i]), int(parts[6 + 2 * i])
                    poly.addPoint(x, y)
                body.add_shape(poly)
            elif prefix == 'S': # Rectangle
                x, y, x2, y2 = [int(i) for i in parts[1:5]]
                rec = shape.Rectangle(x, y, x2 - x, y2 - y)
                body.add_shape(rec)
            elif prefix == 'T': # Text
                angle, x, y = [int(i) for i in parts[1:4]]
                angle = round(angle / 1800.0, 1)
                text = parts[8].replace('~', ' ')
                body.add_shape(shape.Label(x, y, text, 'left', angle))
            elif prefix == 'X': # Pin
                num, direction = int(parts[2]), parts[6]
                p2x, p2y, pinlen = int(parts[3]), int(parts[4]), int(parts[5])
                if direction == 'U': # up
                    p1x = p2x
                    p1y = p2y - pinlen
                elif direction == 'D': # down
                    p1x = p2x
                    p1y = p2y + pinlen
                elif direction == 'L': # left
                    p1x = p2x - pinlen
                    p1y = p2y
                elif direction == 'R': # right
                    p1x = p2x + pinlen
                    p1y = p2y
                else:
                    raise ValueError('unexpected pin direction', direction)
                # TODO: label?
                body.add_pin(Pin(num, (p1x, p1y), (p2x, p2y)))
            elif prefix == 'ENDDEF':
                circuit.add_component(component.name, component)

        f.close()


    def intersect(self, segment, c):
        """ Does point c intersect the segment """
        a,b = segment
        ax,ay, bx,by, cx,cy = a + b + c
        if ax == bx == cx: # Vertical
            if cy > min(ay,by) and cy < max(ay,by): # between a and b
                return True
        elif ay == by == cy: # Horizontal
            if cx > min(ax,bx) and cx < max(ax,bx): # between a and b
                return True
        elif (cx-ax)*(by-ay)==(bx-ax)*(cy-ay): # Diagonal
            if cx > min(ax,bx) and cx < max(ax,bx): # between a and b
                return True
        return False


    def divide(self, segments, junctions):
        """ Divide segments by junctions """
        for c in junctions:
            toremove = set()
            toadd = set()
            for seg in segments:
                if self.intersect(seg,c):
                    a,b = seg
                    toremove.add((a,b))
                    toadd.add((a,c))
                    toadd.add((c,b))
            segments -= toremove
            segments |= toadd
        return segments


    def calc_nets(self, segments):
        """ Return a set of Nets from segments """

        points = {} # (x,y) -> NetPoint

        def get_point(p):
            if p not in points:
                points[p] = NetPoint('%da%d' % p, *p)
            return points[p]

        # turn the (x, y) points into unique NetPoint objects
        segments = set((get_point(p1), get_point(p2)) for p1, p2 in segments)
        nets = []

        # Iterate over the segments, removing segments when added to a net
        while segments:
            seg = segments.pop() # pick a point
            newnet = Net('')
            newnet.connect(seg)
            found = True

            while found:
                found = set()

                for seg in segments: # iterate over segments
                    if newnet.connected(seg): # segment touching the net
                        newnet.connect(seg) # add the segment
                        found.add(seg)

                for seg in found:
                    segments.remove(seg)

            nets.append(newnet)

        return nets
