#!/usr/bin/env python
# converter.py - file format converter to and from Upverter's JSON file format
# Alex Ray ajray@ncsu.edu
import os, re

# Accepted input file types
inputtypes = "kicad"
# Accepted output file types
outputtypes = "foo"


class Circuit:
  def __init__(self):
    self.version = {"file_version":"0.0.1", "tool_name":"Upverter"}
    self.nets = []
  def normalize_points(self):
    """ Connect all of the segments into nets """
class Net:
  def __init__(self):
    self.net_id = ""
    self.points = []
    self.attributes = []
    self.annotations = []
class Point:
  def __init__(self,x,y):
    self.point_id = str(x)+"a"+str(y)
    self.x = x
    self.y = y
class Segment:
  """ Line segments, only used for import before normalizing """
  def __init__(self,x1,y1,x2,y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2

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
    if element == "Wire": # Wire Segment
      x1,y1,x2,y2 = f.readline().split()
      segments.append(Segment(x1,y1,x2,y2))
    else if element == "$Comp": # Component
      pass #TODO(ajray): do something useful
  print segments
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
