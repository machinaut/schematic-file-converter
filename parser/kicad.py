#!/usr/bin/env python
#
# Basic Strategy
# 0) Ignore data except the useful
# 1) Read in all of the segments (and junctions and components)
# 2) Divide all the segments by the junctions
# 3) Calculate the nets from the segments
# 4) Read the part library to figure out pin connectivity [TODO]

from core.design import Design


class KiCAD:
    """ The KiCAD Format Parser """

    def __init__(self):
        pass


    def parse(self, filename):
        """ Parse a kicad file into a design """
        # Rough'n'dirty parsing, assume nothing useful comes before the description
        circuit = Design()
        segments = set() # each wire segment
        junctions = set() # wire junction point (connects all wires under it)
        f = open(filename)
        # Read until the end of the description
        line = ""
        while line.strip() != "$EndDescr":
            line = f.readline()
        # Now parse wires and components, ignore connections, we get connectivity from wire segments
        line = f.readline()
        while line != '': # loop til end of file
            element = line.split()[0] # whats next on the list
            if element == "Wire": # Wire Segment, coords on 2nd line
                line = f.readline() # Read the second line with the coordinates
                x1,y1,x2,y2 = [int(i) for i in line.split()]
                if not(x1 == x2 and y1 == y2): # ignore zero-length segments
                    segments.add(((x1,y1),(x2,y2)))
            elif element == "Connection": # Store these to apply later
                x,y = [int(i) for i in line.split()[2:4]]
                junctions.add((x,y))
            elif element == "$Comp": # Component
                # TODO(ajray): probably should can by leading letter, instead of assuming they're what we expect
                compnames = f.readline()
                name,reference = compnames.split()[1:3]
                unused_timestamp = f.readline()
                positions = f.readline()
                compx,compy = [int(i) for i in f.readline()[1:3]]
                # TODO(ajray): ignore all the fields for now, probably could make these annotations
                line = f.readline()
                while line.strip() != "$EndComp":
                    line = f.readline()
            line = f.readline()
        segments = this.divide(segments,junctions)
        nets = this.calc_nets(segments)
        circuit.nets = nets
        return circuit


    def intersect(self, segment,c):
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


    def divide(self, segments,junctions):
        """ Divide segments by junctions """
        for c in junctions:
            toremove = set()
            toadd = set()
            for seg in segments:
                if this.intersect(seg,c):
                    a,b = seg
                    toremove.add((a,b))
                    toadd.add((a,c))
                    toadd.add((c,b))
            segments -= toremove
            segments |= toadd
        return segments


    def calc_nets(self, asegments):
        """ Return a set of Nets from segments """
        segments = copy.deepcopy(asegments)
        nets = []
        # Iterate over the copied set, removing segments when added to a net
        while len(segments) > 0 :
            seg = segments.pop() # pick a point
            newnet = Net()
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
