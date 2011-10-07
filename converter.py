#!/usr/bin/env python
# converter.py - file format converter to and from Upverter's JSON file format
# Alex Ray ajray@ncsu.edu
# TODO: incorporate part libraries to figure out endpoints
import os, re, copy, json
from optparse import OptionParser

inputtypes = "kicad" # Accepted input file types
outputtypes = "json" # Accepted output file types

class Circuit:
  """ Circuit represents the whole schematic, and the top level of the output format """
  def __init__(self):
    self.version = {"file_version":"0.0.1", "tool_name":"Upverter"}
    self.nets = []
    self.components = []
    self.instances = []
    self.attributes = []
  def json(self):
    """ prettify circuit for json outputting """
    return {
        "version" : self.version,
        "nets" : [i.json() for i in self.nets],
        "components" : self.components,
        "instances" : self.instances,
        "attributes" : self.attributes
        }

class Net:
  """ a Net with metadata and a list of points (with connections) """
  def __init__(self):
    self.net_id = ""
    self.points = {} # dict to make looking up points easier, outputted as array
    self.attributes = []
    self.annotations = []
  def addpoint(self,p):
    """ Add a point p to the net """
    self.points[p] = {
      "point_id": p, #internally use the point tuples as ID's, output as string id's
      "x":p[0],
      "y":p[1],
      "connected_components": [], #TODO(ajray): figure out how to connect to comps
      "connected_points": set()
      }
  def connpoint(self,a,b):
    """ connect point b to point a """
    self.points[a]["connected_points"].add(b)
  def connected(self,seg):
    """ is segment connected to this net """
    a,b = seg
    return a in self.points or b in self.points
  def connect(self,seg):
    """ connect segment to this net """
    a,b = seg
    if a not in self.points:
      self.addpoint(a)
    self.connpoint(a,b)
    if b not in self.points:
      self.addpoint(b)
    self.connpoint(b,a)
  def prettypoints(self):
    """ return points array with point_id's instead of tuples """
    a = self.points.values()
    for p in a:
      p["connected_points"] = [point_id(i) for i in p["connected_points"]]
      p["point_id"] = point_id(p["point_id"])
    return a
  def json(self):
    """ return a dict for json outputting """
    return {
        "attributes":self.attributes,
        "annotations":self.annotations,
        "net_id":self.net_id,
        "points":self.prettypoints()
        }

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
    
def input_kicad(filename):
  """ Read in a kicad schematic file and parse it into Upverter format """
  # Rough'n'dirty parsing, assume nothing useful comes before the description
  circuit = Circuit()
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
  nets = calc_nets(segments)
  circuit.nets = nets
  return circuit

def output_json(circuit, filename):
  """ Placeholder output function until I get the JSON file format """
  f = open(filename, "w")
  f.write(json.dumps(circuit.json(),sort_keys=True,indent=4))
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
  if outputtype == "json":
    output_json(ckt, outputfile)
