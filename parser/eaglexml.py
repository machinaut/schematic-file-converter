#!/usr/bin/env python
#
# Basic Strategy
# 1) Write Parser
# 2) Create Design
# 3) ...
# 4) Profit!

from core.design import Design
from xml.etree.ElementTree import ElementTree


class EagleXML:
    """ The Eagle XML Format Parser """

    def __init__(self):
        pass


    def parse(self, filename):
        circuit = Design()
        #return circuit

        """ Parse an Eagle XML file into a design """
        #import an xmltree from the file provided
       	xmltree = ElementTree(file=filename)
        root = xmltree.getroot()
        drawings = root.findall('drawing')
        for drawing in drawings:
          grids = drawing.findall('grid')
          alllayers = drawing.findall('layers')
          allsettings = drawing.findall('settings')
          schematics = drawing.findall('schematic')
          for schematic in schematics:
            print list(schematic),"\n\n"
            alllibraries = schematic.findall('libraries')
            for libraries in alllibraries:
              for library in libraries:
                pass # this iterates over ALL the libraries
            allattributes = schematic.findall('attributes')
            for attributes in allattributes:
              for attribute in attributes:
                pass
            allvariantdefs = schematic.findall('variantdefs')
            print 'allvardef', list(allvariantdefs)
            for variantdefs in allvariantdefs:
              print 'vardef', list(variantdefs)
              for variantdef in variantdefs:
                pass
            allparts = schematic.findall('parts')
            for parts in allparts:
              for part in parts:
                print part.attrib
            sheets = schematic.findall('sheet')

        return circuit
