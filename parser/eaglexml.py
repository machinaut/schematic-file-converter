#!/usr/bin/env python
#
# Basic Strategy
# 1) Write Parser
# 2) Create Design
# 3) ...
# 4) Profit!

from core.design import *
from core.component import *
from core.instance import *
from core.shape import *
from xml.etree.ElementTree import ElementTree


class EagleXML:
    """ The Eagle XML Format Parser """

    def __init__(self):
        self.parts = dict() # key by part name == instance_id
        self.lib = dict() # key by lib_devset_dev == library_id
        self.gates = dict() # key by gate name
        self.symbols = dict() # key by symbol name
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
                    name = symbol.attrib['name']
                    lib_id = library.attrib['name']+'_'+name
                    # NOTE: this is NOT the correct library_id
                    s = Symbol()
                    b = Body()
                    for wire in symbol.findall('wire'):
                      # TODO: grab the width and layer
                      x1 = int(float(wire.attrib['x1'])*1000)
                      y1 = int(float(wire.attrib['y1'])*1000)
                      x2 = int(float(wire.attrib['x2'])*1000)
                      y2 = int(float(wire.attrib['y2'])*1000)
                      b.add_shape(Line(x1,y1,x2,y2))
                    for text in symbol.findall('text'):
                      # TODO grab the size
                      x = int(float(text.attrib['x'])*1000)
                      y = int(float(text.attrib['y'])*1000)
                      r = 0 # TODO check rotation
                      t = text.text
                      align = 'left' # TODO check that this is never else
                      b.add_shape(Label(x,y,t,align,r))
                    for pin in symbol.findall('pin'):
                      # TODO get pins direction, 
                      n = pin.attrib['name']
                      x = int(float(pin.attrib['x'])*1000)
                      y = int(float(pin.attrib['y'])*1000)
                      p1 = Point(x,y)
                      if pin.attrib.get('rot') == 'R180':
                        x -= 10
                        p2 = Point(x,y)
                      else:
                        x += 10
                        p2 = Point(x,y)
                      # TODO figure out actual default length
                      l = Label(0,0,n,'left',0)
                      b.add_pin(Pin(n,p1,p2,l))
                    s.add_body(b)
                    self.symbols[name] = s
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
                        self.gates[gate.attrib['name']] = gate.attrib
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
                        c = Component(library_id,name)
                        self.lib[library_id] = c
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
                    instance_id = instance.attrib['part']
                    library_id = self.getpartlib(instance_id)
                    gat = instance.attrib.get('gate')
                    symnam = self.gates.get(gat).get('symbol')
                    sym = self.symbols.get(symnam)
                    # TODO leet hax
                    c = Component(library_id,symnam)
                    c.add_symbol(sym)
                    circuit.add_component(c)
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
        print self.symbols
        print self.gates
        print self.lib
        return circuit
