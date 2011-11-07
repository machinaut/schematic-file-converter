#!/usr/bin/env python
#
# Basic Strategy
# 1) Write Parser
# 2) Create Design
# 3) ...
# 4) Profit!

# TODO(ajray): right now its one symbol per component
#     we should properly handle all of Eagle's:
#     libraries, devicesets, devices, packages, and symbols
#     but thats all too complex for right now

from core.design import *
from core.component import *
from core.instance import *
from core.shape import *
from xml.etree.ElementTree import ElementTree


class EagleXML:
    """ The Eagle XML Format Parser """

    def __init__(self):
        self.design = Design()
        # In the order they are parsed:
        self.symbols = dict()   # key:library_id  val:Symbol()
        self.gates = dict()     # key:gate_id     val:{lib,devset,sym}
        self.parts = dict()     # key:instance_id val:{lib,devset,dev}
        pass


    def parse_wire(self,wire):
        # TODO: grab the width and layer
        x1 = int(float(wire.attrib['x1'])*100)
        y1 = int(float(wire.attrib['y1'])*100)
        x2 = int(float(wire.attrib['x2'])*100)
        y2 = int(float(wire.attrib['y2'])*100)
        return Line(x1,y1,x2,y2)


    def parse_text(self,text):
        # TODO grab the size
        x = int(float(text.attrib['x'])*100)
        y = int(float(text.attrib['y'])*100)
        r = 0 # TODO check rotation
        t = text.text
        align = 'left' # TODO check that this is never otherwise
        return Label(x,y,t,align,r)


    def parse_pin(self,pin):
        # TODO get pins direction, 
        n = pin.attrib['name']
        x = int(float(pin.attrib['x'])*100)
        y = int(float(pin.attrib['y'])*100)
        p1 = Point(x,y)
        # TODO handle all of the rotations
        if pin.attrib.get('rot') == 'R180':
          x -= 10
          p2 = Point(x,y)
        else:
          x += 10
          p2 = Point(x,y)
        # TODO figure out actual default pin length
        l = Label(0,0,n,'left',0)
        return Pin(n,p1,p2,l)


    def parse_symbol(self,library,symbol):
        # Make the Body
        # TODO handle multi-body symbols
        b = Body()
        for wire in symbol.findall('wire'):
          b.add_shape(self.parse_wire(wire))
        for text in symbol.findall('text'):
          b.add_shape(self.parse_text(text))
        for pin in symbol.findall('pin'):
          b.add_pin(self.parse_pin(pin))

        # Make the Symbol
        s = Symbol()
        s.add_body(b)
        lib  = library.attrib.get('name')
        sym = symbol.attrib.get('name')
        library_id = lib + '_' + sym
        self.symbols[library_id] = s

        # Make the Component
        # TODO handle multi-symbol components; now a comp for each symbol
        c = Component(library_id,sym)
        c.add_symbol(s)

        # Add the Component (and Symbol and Body)
        self.design.add_component(c)


    def parse_gate(self,library,deviceset,gate):
        lib     = library.attrib.get('name')
        devset  = deviceset.attrib.get('name')
        sym     = gate.attrib.get('symbol')
        gat     = gate.attrib.get('name')
        gate_id = lib + '_' + gat
        self.gates[gate_id] = {"library" : lib,
                               "deviceset" : devset, 
                               "symbol" : sym}
        

    def parse_part(self, part):
        instance_id = part.attrib.get('name')
        self.parts[instance_id] = {
            "library"   : part.attrib.get('library'),
            "deviceset" : part.attrib.get('deviceset'),
            "device"    : part.attrib.get('device') }


    def parse_instance(self,instance):
        instance_id = instance.attrib.get('part')
        # Figure out library_id from part->gate/library->symbol
        part_dict = self.parts.get(instance_id)
        gat = instance.attrib.get('gate')
        lib = part_dict.get('library')
        gate_id = lib + '_' + gat
        gate_dict = self.gates.get(gate_id)
        sym = gate_dict.get('symbol')
        library_id = lib + '_' + sym # figured out

        # Make the Instance()
        symbol_index = 0 # TODO handle multi-symbol components
        inst = Instance(instance_id, library_id, symbol_index)

        # Make the instance's symbol_attribute
        # TODO handle multi-body symbols
        x = int(float(instance.attrib['x'])*100)
        y = int(float(instance.attrib['y'])*100)
        rotation = 0 # TODO get the real rotation
        sa = SymbolAttribute(x,y,rotation)
        inst.add_symbolattribute(sa)

        # Add Instance to the design
        self.design.add_instance(inst)


    def parse(self, filename):
        """ Parse an Eagle XML file into a design """
        xmltree = ElementTree(file=filename)
        root = xmltree.getroot()
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
                    self.parse_symbol(library,symbol)
                for devicesets in library.findall('devicesets'):
                  for deviceset in devicesets.findall('deviceset'):
                    #print "DEVICESET", list(deviceset), deviceset.attrib
                    for description in deviceset.findall('description'):
                      #print "DESCRIPTION", description.text, \
                      #    list(description), description.attrib
                      pass
                    for gates in deviceset.findall('gates'):
                      for gate in gates.findall('gate'):
                        self.parse_gate(library,deviceset,gate)
                    for devices in deviceset.findall('devices'):
                      for device in devices.findall('device'):
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
                self.parse_part(part)
            for sheets in schematic.findall('sheets'):
              for sheet in sheets.findall('sheet'):
                for plain in sheet.findall('plain'):
                  for text in plain.findall('text'):
                    pass
                for instances in sheet.findall('instances'):
                  for instance in instances.findall('instance'):
                    self.parse_instance(instance)
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
        print self.gates
        print self.symbols
        print self.parts
        return self.design
      

