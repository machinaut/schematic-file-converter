#!/usr/bin/env python
#
# upconvert.py - A universal hardware design file format converter using
# Upverter's Open JSON Interchange Format
# (http://upverter.com/resources/open-json-format/)
#
# Authors:
#   Alex Ray ajray@ncsu.edu
#   Upverter support@upverter.com
#
# Usage example:
#   ./upconvert.py -i test.upv -o test.json 


import os, re, copy, json
import parser.openjson, parser.kicad
import parser.eaglexml
import writer.openjson, writer.kicad
from argparse import ArgumentParser

parsers = {
    'openjson': parser.openjson.JSON,
    'kicad': parser.kicad.KiCAD,
    'eaglexml': parser.eaglexml.EagleXML
}

writers = {
    'openjson': writer.openjson.JSON,
    'kicad': writer.kicad.KiCAD
}


def parse(f, format='openjson'):
    try:
        p = parsers[format]()
    except KeyError:
        print "ERROR: Unsupported input type:", format
        exit(1)
    return p.parse(f)


def write(d, f, format='openjson'):
    try:
        w = writers[format]()
    except KeyError:
        print "ERROR: Unsupported output type:", format
        exit(1)
    return w.write(d, f)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i","--input", dest="inputfile",help="read INPUT file in",
            metavar="INPUT")
    parser.add_argument("-f","--from", dest="inputtype",help="read input file as TYPE",
            metavar="TYPE", default="openjson")
    parser.add_argument("-o","--output", dest="outputfile",help="write OUTPUT file out",
            metavar="OUTPUT")
    parser.add_argument("-t","--to", dest="outputtype",help="write output file as TYPE",
            metavar="TYPE", default="openjson")

    args = parser.parse_args()
    inputtype = args.inputtype
    outputtype = args.outputtype
    inputfile = args.inputfile
    outputfile = args.outputfile
    if None == inputfile:
      parser.print_help()
      exit(1)

    # parse and export the data
    design = parse(inputfile, inputtype)
    write(design, outputfile, outputtype)
