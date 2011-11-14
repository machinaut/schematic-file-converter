#!/usr/bin/env python
#
# Basic Strategy
# 1) read all symbols into self.symbols
# 2) read all gates (instances of symbols) into self.gates
# 3) read all parts (relation instance->library) into self.parts
# 3) read all instances (locations of instances) and use self.parts,
#       self.gates, and self.symbols to connect to it's symbol

# TODO(ajray): right now its one symbol per component
#     we should properly handle all of Eagle's:
#     libraries, devicesets, devices, packages, and symbols
#     but thats all too complex for right now
# TODO(ajray): check the DTD against eagle.dtd

import math
from core.design import *
from core.component_instance import *
from core.components import *
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
        self.scale = 10./2.54  # TODO: figure out a way to infer this


    def parse(self, filename):
        """ Parse an Eagle XML file into a design """
        xmltree = ElementTree(file=filename)
        root = xmltree.getroot()
        drawings = root.findall('drawing')
        for drawing in drawings:
            #for grid in drawing.findall('grid'):
            #for layers in drawing.findall('layers'):
            #    for layer in layers.findall('layer'):
            #for settings in drawing.findall('settings'):
            #    for setting in settings.findall('settings'):
            for schematic in drawing.findall('schematic'):
                self.parse_schematic(schematic)
        print 'symbols\n',self.symbols.keys()
        print 'gates\n',self.gates.keys()
        print 'parts\n',self.parts.keys()
        return self.design


    def parse_schematic(self, schematic):
        for libraries in schematic.findall('libraries'):
            for library in libraries.findall('library'):
                self.parse_library(library)
        #for attributes in schematic.findall('attributes'):
        #    for attribute in attributes.findall('attribute'):
        #for variantdefs in schematic.findall('variantdefs'):
        #    for variantdef in variantdefs.findall('variantdef'):
        #for classes in schematic.findall('classes'):
        #    for class_ in classes.findall('class'):
        for parts in schematic.findall('parts'):
            for part in parts.findall('part'):
                self.parse_part(part)
        for sheets in schematic.findall('sheets'):
            for sheet in sheets.findall('sheet'):
                self.parse_sheet(sheet)


    def parse_library(self,library):
        #for description in library.findall('description'):
        #for packages in library.findall('packages'):
        #    for package in packages.findall('package'):
        for symbols in library.findall('symbols'):
            for symbol in symbols.findall('symbol'):
                self.parse_symbol(library,symbol)
        for devicesets in library.findall('devicesets'):
            for deviceset in devicesets.findall('deviceset'):
                self.parse_deviceset(library,deviceset)
      

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
        c = Component(sym)
        c.add_symbol(s)

        # Add the Component (and Symbol and Body)
        self.design.add_component(library_id,c)


    def parse_wire(self,wire):
        # TODO: grab the width and layer
        x1 = int(round(float(wire.attrib['x1'])*self.scale,-0))
        y1 = int(round(float(wire.attrib['y1'])*self.scale,-0))
        x2 = int(round(float(wire.attrib['x2'])*self.scale,-0))
        y2 = int(round(float(wire.attrib['y2'])*self.scale,-0))
        curve = wire.attrib.get('curve')
        if curve is None:
            p1 = Point(x1,y1)
            p2 = Point(x2,y2)
            return Line(p1,p2)
        else: # curve is not None:
            # give the angle in pi radians
            angle = math.radians(round(float(curve)),-1)/math.pi
            return self.parse_curve(x1,y1,x2,y2,angle)


    def parse_curve(self,x1,y1,x2,y2,angle):
        # TODO: add this mathematical def'n of an arc to core/shape.py
        # TODO: more general form of an arc. right now just restricted to
        #   Multiples of right angles. Adding special cases as necessary
        if -0.5 == angle:
            x1,y1,x2,y2 = x2,y2,x1,y1 # switch points
            angle = 0.5
        if 0.5 == angle:
            pass
        return Arc(xc,yc,start_angle,end_angle,int(R))



    def parse_text(self,text):
        # TODO grab the size
        x = int(round(float(text.attrib['x'])*self.scale,-0))
        y = int(round(float(text.attrib['y'])*self.scale,-0))
        r = 0 # TODO check rotation
        t = text.text
        align = 'left' # TODO check that this is never otherwise
        return Label(x,y-5,t,align,r)


    def parse_pin(self,pin):
        # TODO get pins direction, 
        length = pin.attrib.get('length')
        # TODO handle zero-length pins
        if 'long' == length:
            off = 30
        elif 'middle' == length:
            off = 20
        #elif 'point' == length:
        #    off = 0
        else: # 'short' == length, and default
            off = 10
        n = pin.attrib.get('name')
        x = int(round(float(pin.attrib['x'])*self.scale,-0))
        y = int(round(float(pin.attrib['y'])*self.scale,-0))
        p2 = Point(x,y)
        # TODO handle all of the rotations
        if pin.attrib.get('rot') == 'R180':
          x -= off
          p1 = Point(x,y)
          l = Label(x-5,y-5,n,'right',0)
        else:
          x += off
          p1 = Point(x,y)
          l = Label(x+5,y-5,n,'left',0)
        # TODO figure out actual default pin length
        return Pin(n,p1,p2,l)
        

    def parse_deviceset(self,library,deviceset):
        #for description in deviceset.findall('description'):
        for gates in deviceset.findall('gates'):
            for gate in gates.findall('gate'):
                self.parse_gate(library,deviceset,gate)
        #for devices in deviceset.findall('devices'):
        #    for device in devices.findall('device'):


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


    def parse_sheet(self,sheet):
        #for plain in sheet.findall('plain'):
        #    for text in plain.findall('text'):
        for instances in sheet.findall('instances'):
            for instance in instances.findall('instance'):
                self.parse_instance(instance)
        #for busses in sheet.findall('busses'):
        #for nets in sheet.findall('nets'):
        #    for net in nets.findall('net'):
        #        for segment in net.findall('segment'):
        #            for wire in segment.findall('wire'):
        #            for junction in segment.findall('junction'):
        #            for pinref in segment.findall('pinref'):
        

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

        # Make the ComponentInstance()
        symbol_index = 0 # TODO handle multi-symbol components
        inst = ComponentInstance(instance_id, library_id, symbol_index)

        # Make the instance's symbol_attribute
        # TODO handle multi-body symbols
        x = int(round(float(instance.attrib['x'])*self.scale,-0))
        y = int(round(float(instance.attrib['y'])*self.scale,-0))
        rotation = 0 # TODO get the real rotation
        sa = SymbolAttribute(x,y,rotation)
        inst.add_symbol_attribute(sa)

        # Add ComponentInstance to the design
        self.design.add_component_instance(inst)


class Schematic:
    def __init__(self):
        self.libraries = dict()
        self.parts = dict()
        self.sheets = list()
    def add_library(self,library_id,library):
        self.libraries[library_id] = library
    def add_part(self,part_id,part):
        self.parts[part_id] = part
    def add_sheet(self,sheet):
        self.sheets.append(sheet)

class Library:
    def __init__(self,name):
        self.name = name
        self.packages = dict()
        self.symbols = dict()
        self.devicesets = dict()
    def add_package(self,name,package):
        self.packages[name] = package
    def add_symbol(self,name,symbol):
        self.symbols[name] = symbol
    def add_deviceset(self,name,deviceset):
        self.devicesets[name] = deviceset
class Part:
    def __init__(self,name,library,deviceset,device,value=None):
        self.name = name
        self.library = library
        self.deviceset = deviceset
        self.device = device
        self.value = value
class Sheet:
    def __init__(self):
        self.shapes = list()
        self.instances = dict() # key:("part","gate")
        self.busses = None # TODO: parse busses
        self.nets = dict()
    def add_shape(self,shape):
        self.shapes.append(shape)
    def add_instance(self,part,gate,instance):
        self.instances[(part,gate)] = instance
    def add_net(self,name,net):
        self.nets[name] = net
class Instance:
    def __init__(self,part,gate,x,y,rot)
class Package:
    def __init__(self,name):
        self.name = name
        self.shapes = list()
    def add_shape(self,shape):
        self.shapes.append(shape)
class Symbol:
    def __init__(self,name):
        self.name = name
        self.shapes = list()
    def add_shape(self,shape):
        self.shapes.append(shape)
class Deviceset:
    def __init__(self,name,prefix=None):
        self.name = name
        self.prefix = prefix
        self.description = ""
        self.gates = dict()
        self.devices = dict()
    def set_description(self,description):
        self.description = description
    def add_gate(self,name,gate):
        self.gates[name] = gate
    def add_device(self,name,device):
        self.devices[name] = device
class Gate:
    def __init__(self,name,symbol,x,y,addlevel=None):
        self.name = name
        self.symbol = symbol
        self.x = x
        self.y = y
        self.addlevel = addlevel # TODO figure out what this does
class Device:
    def __init__(self,name,package=None):
        self.name = name
        self.package = package
        self.connects = list()
    def add_connect(self,connect)
        self.connects.append(connect)
class Connect:
    def __init__(self,gate,pin,pad):
        self.gate = gate
        self.pin = pin
        self.pad = pad
