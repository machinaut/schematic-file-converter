#!/usr/bin/env python
# converter.py - file format converter to and from Upverter's JSON file format
# Alex Ray ajray@ncsu.edu
import os, re, copy

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

def intersect(segment,c):
  """ Do they intersect; Assuming orthogonal """
  a,b = segment
  if a[0] == b[0] == c[0]:
    if c[1] >= min(a[1],b[1]) and c[1] <= max(a[1],b[1]):
      return a[1] != c[1] and b[1] != c[1]
  elif a[1] == b[1] == c[1]:
    if c[0] >= min(a[0],b[0]) and c[0] <= max(a[0],b[0]):
      return a[0] != c[0] and b[0] != c[0]
  return False

def connect(segments,c):
  """ Apply a connection point to a set of segments """
  i = 0
  toremove = set()
  toadd = set()
  for seg in segments:
    if seg == ((6100,4650),(6100,5350)):
      print "WTF", intersect(seg,c), seg, c
    if intersect(seg,c):
      print 'counter', i
      i += 1
      print 'im connected to',seg
      print 'before',seg
      a,b = seg
      toremove.add((a,b))
      print 'after',(a,c),(c,b)
      toadd.add((a,c))
      toadd.add((c,b))
  return (segments - toremove) | toadd
    
def connections(segments):
  """ Return the connecting points of a list of segments """
  conns = {}
  for seg in segments:
    a,b = seg
    conns[a] = {a,b}
    conns[b] = {a,b}
    for otherseg in segments:
      oa, ob = otherseg
      if a == ob:
        conns[a].add(oa)
      elif a == oa:
        conns[a].add(ob)
      if b == ob:
        conns[b].add(oa)
      elif b == oa:
        conns[b].add(ob)
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
      nets.append({conns.keys()[0]}) # pick a point
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
    elif element == "Connection": # connecting dot
      x,y = [int(i) for i in line.split()[2:4]]
      connpoints.add((x,y))
    elif element == "$Comp": # Component
      pass #TODO(ajray): do something useful
    line = f.readline()
  #TODO(ajray): XXX Horribly nasty
  for c in connpoints: segments = connect(segments,c)
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
  a = (6100,5350)
  b = (6100,4650)
  c = (6100,4950)
  print 'intersect:', a,b,c, "is actually", intersect((a,b),c)
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
