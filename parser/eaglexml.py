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
        """ Parse an Eagle XML file into a design """
        circuit = Design()

        #import an xmltree from the file provided
       	xmltree = ElementTree(file=filename)
        root = xmltree.getroot()
        # use elem.findall() to make sure to iterate over duplicates
        drawings = root.findall('drawing')
        for drawing in drawings:
          for grid in drawing.findall('grid'):
            #print "GRID", list(grid), grid.attrib
            pass
          for layers in drawing.findall('layers'):
            for layer in layers.findall('layer'):
              #print "LAYER", list(layer), layer.attrib
              pass
          for settings in drawing.findall('settings'):
            for setting in settings.findall('settings'):
              #print "SETTING", list(setting), setting.attrib
              pass
          for schematic in drawing.findall('schematic'):
            print "SCHEMATIC", list(schematic), schematic.attrib
            for libraries in schematic.findall('libraries'):
              for library in libraries.findall('library'):
                print "LIBRARY", list(library), library.attrib
                for description in library.findall('description'):
                  #print "DESCRIPTION", description.text, \
                  #    list(description), description.attrib
                  pass
                for packages in library.findall('packages'):
                  for package in packages.findall('package'):
                    #print "PACKAGE", package.attrib
                    pass
                for symbols in library.findall('symbols'):
                  for symbol in symbols.findall('symbol'):
                    #print "SYMBOL", symbol.attrib
                    pass
                for devicesets in library.findall('devicesets'):
                  for deviceset in devicesets.findall('deviceset'):
                    print "DEVICESET", list(deviceset), deviceset.attrib
                    pass
            for attributes in schematic.findall('attributes'):
              for attribute in attributes.findall('attribute'):
                pass # this iterates over ALL the attributes
            for variantdefs in schematic.findall('variantdefs'):
              for variantdef in variantdefs.findall('variantdef'):
                pass # this iterates over ALL the variantdefs
            for classes in schematic.findall('classes'):
              for class_ in classes.findall('class'):
                pass # this iterates over ALL the classes
            for parts in schematic.findall('parts'):
              for part in parts.findall('part'):
                pass # this iterates over ALL the parts
            for sheets in schematic.findall('sheets'):
              for sheet in sheets.findall('sheet'):
                for plain in sheet.findall('plain'):
                  for text in plain.findall('text'):
                    pass
                for instances in sheet.findall('instances'):
                  for instance in instances.findall('instance'):
                    pass
                for busses in sheet.findall('busses'):
                  pass
                for nets in sheet.findall('nets'):
                  for net in nets.findall('net'):
                    for segment in net.findall('segment'):
                      for wire in segment.findall('wire'):
                        pass
                      for junction in segment.findall('junction'):
                        pass
                      for pinref in segment.findall('pinref'):
                        print list(pinref), pinref.attrib
                        pass

        return circuit
