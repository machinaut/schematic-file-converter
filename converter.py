#!/usr/bin/env python
# converter.py - file format converter to and from Upverter's JSON file format
# Alex Ray ajray@ncsu.edu
import os, re

# Accepted input file types
inputtypes = "kicad"
# Accepted output file types
outputtypes = "foo"

def input_kicad(filename):
  """ Read in a kicad schematic file and parse it into Upverter format """
  f = open(filename)
  header = f.readline() # Should match EESchema Schematic Spins Version ### ...
  head = re.search("EESchema\s*Schematic\s*Spins\s*Version\s*(\d+)",header)
  if not head: # Failed to match header
    print "WARNING: Failed to recognize Kicad Schematic Header:", header
  circuit = "Kicad Version: " + str(head.group(1)) + "\n"
  # Ignore all the libraries
  line = f.readline()
  while "LIB" in line:
    line = f.readline()
  # EElayer, should be next two lines
  eelayer = re.search("EELAYER\s+(\d+)\s+(\d+)\s+EELAYER\s*END",line + f.readline())
  if not eelayer: # Failed to match EELAYER
    print "WARNING: Failed to recognize EELAYER lines"
  circuit += "EELAYER " + eelayer.group(1) + " " + eelayer.group(2) + "\n"
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
