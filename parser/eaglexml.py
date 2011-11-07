#!/usr/bin/env python
#
# Basic Strategy
# 1) Write Parser
# 2) Create Design
# 3) ...
# 4) Profit!

from core.design import Design
from core.component import Component
from core.instance import Instance,SymbolAttribute
from xml.etree.ElementTree import ElementTree


class EagleXML:
    """ The Eagle XML Format Parser """

    def __init__(self):
        self.parts = dict() # key by part name == instance_id
        self.lib = dict() # key by lib_devset_dev == library_id
        pass

    def getpartlib(self,name):
        spn = self.parts[name]
        return '_'.join([spn['library'],spn['deviceset'],spn['device']])

    def newinstance(self,inst):
        instance_id = inst['part']
        library_id = self.getpartlib(instance_id)
        symbol_index = 0 # TODO get me some of this
        instance = Instance(instance_id, library_id, symbol_index)
        instance.add_attribute('gate',inst['gate'])
        # TODO make this conversion nicer, use the grid
        x,y = int(float(inst['x'])*1000),int(float(inst['y'])*1000)
        # TODO get a real rotation
        sa = SymbolAttribute(x,y,0)
        # TODO make a cogent SymbolAttribute
        instance.add_symbolattribute(sa)
        return instance

    def parse(self, filename):
        """ Parse an Eagle XML file into a design """
        circuit = Design()

        #import an xmltree from the file provided
       	xmltree = ElementTree(file=filename)
        root = xmltree.getroot()
        # use elem.findall() to make sure to iterate over duplicates
        drawings = root.findall('drawing')
        for drawing in drawings:
          #print "DRAWING", list(drawing), drawing.attrib
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
            #print "SCHEMATIC", list(schematic), schematic.attrib
            for libraries in schematic.findall('libraries'):
              for library in libraries.findall('library'):
                #print "LIBRARY", list(library), library.attrib
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
                    #print "DEVICESET", list(deviceset), deviceset.attrib
                    for description in deviceset.findall('description'):
                      #print "DESCRIPTION", description.text, \
                      #    list(description), description.attrib
                      pass
                    for gates in deviceset.findall('gates'):
                      for gate in gates.findall('gate'):
                        #print "GATE", gate.attrib
                        pass
                    for devices in deviceset.findall('devices'):
                      for device in devices.findall('device'):
                        #print "DEVICES", device.attrib
                        # there be japage's here
						library_id = '_'.join(
								[library.attrib['name'],
								deviceset.attrib['name'],
								device.attrib['name']])
						name = device.attrib['name']
						attributes = {}
						symbols = {}
						

                        #pass
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
                d = part.attrib
                self.parts[d['name']] = d
                pass # this iterates over ALL the parts
            #print "PARTS DICT:", self.parts
            for sheets in schematic.findall('sheets'):
              for sheet in sheets.findall('sheet'):
                for plain in sheet.findall('plain'):
                  for text in plain.findall('text'):
                    pass
                for instances in sheet.findall('instances'):
                  for instance in instances.findall('instance'):
                    i = self.newinstance(instance.attrib)
                    circuit.add_instance(i)
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
                        pass
        return circuit
