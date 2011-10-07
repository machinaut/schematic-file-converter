#!/usr/bin/env python
# converter.py - file format converter to and from Upverter's JSON file format
# Alex Ray ajray@ncsu.edu
import os, re, copy

# Accepted input file types
inputtypes = "kicad"
# Accepted output file types
outputtypes = "foo"

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

class Segment:
  """ Line segments, only used for import before normalizing """
  def __init__(self,x1,y1,x2,y2):
    self.x1 = int(x1)
    self.y1 = int(y1)
    self.x2 = int(x2)
    self.y2 = int(y2)
    self.a = (x1,y1)
    self.b = (x2,y2)
  def __str__(self):
    return str([(self.x1,self.y1),(self.x2,self.y2)])
  def connected(self,x,y):
    """ Is a point connected with either of the segment's points """
    return (x == self.x1 and y == self.y1) or (x == self.x2 and y == self.y2)
  def intersect(self,x,y):
    """ does this point intersect (on top of) this segment, ASSUME ORTHOGONAL """
    if self.x1 == self.x2:
      return (y >= self.y1 and y <= self.y2) or (y <= self.y1 and y >= self.y2)
    # else self.y1 == self.y2:
    return (x >= self.x1 and x <= self.x2) or (x <= self.x1 and x >= self.x2)

def connect(segments,x,y):
  """ Apply a connection point to a set of segments """
  print "connection at:",x,y
  for i in range(len(segments)):
    seg = segments[i]
    if seg.intersect(x,y):
      print 'im connected'
      x1,y1,x2,y2 = seg.x1, seg.y1, seg.x2, seg.y2
      del segments[i]
      segments.append(Segment(x1,y1,x,y))
      segments.append(Segment(x,y,x2,y2))
  return segments
    
def connections(segments):
  """ Return the connecting points of a list of segments """
  conns = {}
  for seg in segments:
    conns[seg.a] = set([seg.a,seg.b])
    conns[seg.b] = set([seg.a,seg.b])
    for otherseg in segments:
      if seg.a == otherseg.b:
        conns[seg.a].add(otherseg.a)
      elif seg.a == otherseg.a:
        conns[seg.a].add(otherseg.b)
      if seg.b == otherseg.b:
        conns[seg.b].add(otherseg.a)
      elif seg.b == otherseg.a:
        conns[seg.b].add(otherseg.b)
  return conns

def make_nets(conns):
  """ Return a list of Nets from connected points """
  conns = copy.deepcopy(conns)
  nets = []
  while len(conns) > 0 :
    found = []
    for c,pts in conns.iteritems():
      for i in range(len(nets)):
        if nets[i] & pts: # overlapping sets
          nets[i] |= pts # add all of the points
          found.append(c)
    for c in found: # remove connections we've already added
      del conns[c]
    if not found: # didnt find anything
      nets.append(set([conns.keys()[0]])) # pick a point
  return nets
    
def input_kicad(filename):
  """ Read in a kicad schematic file and parse it into Upverter format """
  # Rough'n'dirty parsing, assume nothing useful comes before the description
  circuit = {}
  segments = [] # used only to figure out connectivity
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
      x1,y1,x2,y2 = line.split()
      if not(x1 == x2 and y1 == y2): # ignore zero-length segments
        segments.append(Segment(x1,y1,x2,y2))
    elif element == "Connection": # connecting dot
      x,y = line.split()[2:4]
      segments = connect(segments,x,y)
    elif element == "$Comp": # Component
      pass #TODO(ajray): do something useful
    line = f.readline()
  print "SEGMENTS"
  for seg in segments: print seg
  conns = connections(segments)
  print "CONNECTIONS"
  for conn,pts in conns.iteritems(): print conn,pts # Find connected points
  print "NETS"
  for net in make_nets(conns): print net
  return circuit

# TODO(ajray): get the actual output format
def output_foo(circuit, filename):
  """ Placeholder output function until I get the JSON file format """
  f = open(filename, "w")
  f.write(str(circuit)+"\n")
  f.close()

if __name__ == "__main__":
  from optparse import OptionParser
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
