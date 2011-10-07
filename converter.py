#!/usr/bin/env python
# converter.py - file format converter to and from Upverter's JSON file format
# Alex Ray ajray@ncsu.edu
# TODO: incorporate part libraries to figure out endpoints
import os, re, copy, json
from optparse import OptionParser

inputtypes = "kicad" # Accepted input file types
outputtypes = "foo" # Accepted output file types

class Circuit:
  """ Circuit represents the whole schematic, and the top level of the output format """
  def __init__(self):
    self.version = {"file_version":"0.0.1", "tool_name":"Upverter"}
    self.nets = []
  def normalize_points(self):
    """ Connect all of the segments into nets """

class Net:
  """ Net represents a single net, made of lots of points and connections """
  def __init__(self):
    self.net_id = ""
    self.points = []
    self.attributes = []
    self.annotations = []
  def point(self,p,l):
    """ Add a point p which is connected to a list of points l """
    self.points.append({
      "point_id": point_id(p),
      "x":p[0],
      "y":p[1],
      "connected_components": [], #TODO(ajray): figure out how to connect to comps
      "connected_points": [point_id(i) for i in l if i != p]
      })

def point_id(p):
  """ point_id gives a point id of the form XXXXaYYYY, which is unique for points """
  return str(p[0])+"a"+str(p[1])

def intersect(segment,c):
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

def divide(segments,connpoints):
  """ Divide segments by connection points """
  for c in connpoints:
    toremove = set()
    toadd = set()
    for seg in segments:
      if intersect(seg,c):
        a,b = seg
        toremove.add((a,b))
        toadd.add((a,c))
        toadd.add((c,b))
    segments -= toremove
    segments |= toadd
  return segments
    
def calc_nets(asegments):
  """ Return a set of Nets from segments """
  segments = copy.deepcopy(asegments)
  nets = set()
  # Iterate over the copied set, removing segments when added to a net
  while len(segments) > 0 :
    a,b = segments.pop() # pick a point
    newnet = {a,b}
    found = True
    while found:
      found = set()
      for seg in segments: # iterate over segments
        for p in newnet:   # then over points currently in the net
          a,b = seg
          if p == a or p == b: # this segment connects to the net
            found.add(seg)
      for seg in found:
        a,b = seg
        segments.remove(seg)
        newnet |= {a,b}
    nets.add(frozenset(newnet))
  return nets
    
def input_kicad(filename):
  """ Read in a kicad schematic file and parse it into Upverter format """
  # Rough'n'dirty parsing, assume nothing useful comes before the description
  circuit = {}
  segments = set()    # each wire segment
  connpoints = set() # wire connection (connects all wires under it)
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
      connpoints.add((x,y))
    elif element == "$Comp": # Component
      pass #TODO(ajray): do something useful
    line = f.readline()
  segments = divide(segments,connpoints)
  print "NETSNETS"
  for net in calc_nets(segments): print net
  return circuit

# TODO(ajray): get the actual output format
def output_foo(circuit, filename):
  """ Placeholder output function until I get the JSON file format """
  f = open(filename, "w")
  f.write(str(circuit)+"\n")
  f.close()

if __name__ == "__main__":
  parser = OptionParser()
  parser.add_option("-i","--input", dest="inputfile",help="read INPUT file in",metavar="INPUT")
  parser.add_option("-f","--from", dest="inputtype",help="read input file as TYPE",metavar="TYPE")
  parser.add_option("-o","--output", dest="outputfile",help="write OUTPUT file out",metavar="OUTPUT")
  parser.add_option("-t","--to", dest="outputtype",help="write output file as TYPE",metavar="TYPE")
  (options, args) = parser.parse_args()
  print "options,args:", options,args
  # TODO(ajray): intelligently guess input and output types, for now assume explicitly given
  #   partly because most EDA's use '.sch' as the schematic file extension
  inputtype = options.inputtype
  outputtype = options.outputtype
  inputfile = options.inputfile
  outputfile = options.outputfile
  if inputtype not in inputtypes:
    print "ERROR: Unsupported input type:", inputtype
    exit(1)
  if outputtype not in outputtypes:
    print "ERROR: Unsupported output type:", outputtype
    exit(1)
  if inputtype == "kicad":
    ckt = input_kicad(inputfile)
  if outputtype == "foo":
    output_foo(ckt, outputfile)
