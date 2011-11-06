#!/usr/bin/env python
#
# upconvert.py - A universal hardware design file format converter using
# Upverter's Open JSON Interchange Format
#
# Authors:
#   Alex Ray ajray@ncsu.edu
#   Upverter support@upverter.com
#
# Usage example:
#   ./upconvert.py -i test.sch -o test.json -f kicad -t json


import os, re, copy, json
import parser.json, parser.kicad
import writer.json, writer.kicad
from optparse import OptionParser

parsers = {
    'json': parser.json.JSON,
    'kicad': parser.kicad.KiCAD
}

writers = {
    'json': writer.json.JSON,
    'kicad': writer.kicad.KiCAD
}


def parse(f, format='kicad'):
    try:
        p = parsers[format]()
        return p.parse(f)
    except KeyError:
        print "ERROR: Unsupported input type:", format
        exit(1)


def write(d, f, format='json'):
    try:
        w = writers[format]()
        return w.write(d, f)
    except KeyError:
        print "ERROR: Unsupported output type:", format
        exit(1)


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i","--input", dest="inputfile",help="read INPUT file in",metavar="INPUT")
    parser.add_option("-f","--from", dest="inputtype",help="read input file as TYPE",metavar="TYPE")
    parser.add_option("-o","--output", dest="outputfile",help="write OUTPUT file out",metavar="OUTPUT")
    parser.add_option("-t","--to", dest="outputtype",help="write output file as TYPE",metavar="TYPE")

    # parse options
    (options, args) = parser.parse_args()
    print "options,args:", options,args
    inputtype = options.inputtype
    outputtype = options.outputtype
    inputfile = options.inputfile
    outputfile = options.outputfile

    # parse and export the data
    design = parse(inputfile, inputtype)
    write(design, outputfile, outputtype)
