#!/usr/bin/env python
#
# Basic Strategy
# 1) read all symbols into self.symbols
# 2) read all gates (instances of symbols) into self.gates
# 3) read all parts (relation instance->library) into self.parts
# 3) read all instances (locations of instances) and use self.parts,
#       self.gates, and self.symbols to connect to it's symbol
#
# NOTE: The overall order of this file is a class for every element type in doc/eagle.dtd
# NOTE: I've added most of the looping structures (for x in y.findall('foo'))
#       for each element thats given in eagle.dtd.  Unused ones are left
#       commented out or empty, but exist for reference in case they're used later
# NOTE: Someone at CADSoft needs to be taught how to do better XML, so theres lots of 
#       silly redundancy, like having a <settings> tag that contains a bunch of <setting> tags
#       (instead of just having all the <setting>s at the top level). We're not using
#       Separate parsing functions for the plurality.
# NOTE: In cases where there is an optional element (zero or one of it) we will
#       Happily parse multiples, with each one clobbering the last. TODO: generate a 
#       soft warning when this happens
# NOTE: Not all parse_* functions are created equal.  Some modify the design (self) tree,
#       while others do not alter state and instead return an object.  TODO: change the non-
#       state altering parse_* functions that return objects into make_* functions instead
#
# TODO(ajray): right now its one symbol per component
#     we should properly handle all of Eagle's:
#     libraries, devicesets, devices, packages, and symbols
#     but thats all too complex for right now
# TODO(ajray): check the DTD against eagle.dtd
# TODO(ajray): could possibly auto-generate a parser from the dtd,
#     converted to an xsd (I've already done this, it's in doc/)
#     Huge amount of generated spaghetti code, but could save time
#     in writing an output parser.
# TODO(ajray): make a custom exception to throw on parsing error,
#     handle it gracefully in upconvert.py 
# TODO(ajray): figure out a way to give back soft warnings (non-fatal issues)
# TODO(ajray): I have the hierarchy of bodies and symbols in the parsed schematic wonky
# TODO(ajray): Having each class check it's tag to verify would be great. Though I
#     can't imagine them being called outside of this file (so that shouldnt happen)


import math
from core.design import *
from core.component_instance import *
from core.components import *
from core.shape import *
from xml.etree.ElementTree import ElementTree

SCALE = 10./2.54   # TODO: figure out a way to infer this

class EagleXML:
    """ 
    The Eagle XML Format Parser 
    Built referencing the eagle.dtd that comes with Eagle 6 Beta
    """
    def __init__(self):
        self.design = Design()
        # In the order they are parsed:
        self.symbols = dict()   # key:library_id  val:Symbol()
        self.gates = dict()     # key:gate_id     val:{lib,devset,sym}
        self.parts = dict()     # key:instance_id val:{lib,devset,dev}
        self.version = None     # EAGLE program version that generated this file ('V.RR')

    def parse(self, filename):
        """ Parse an Eagle XML file into a design """
        xmltree = ElementTree(file=filename)
        root = xmltree.getroot()
        # Verify the root tag, beginning what is essentially
        if root.tag.lower() != "eagle":
            print "ERROR reading eagle XML file, root tag is not 'eagle'"
            return None
        eagle = Eagle(root)


class Eagle:
    def __init__(self, eagle):
        self.version = eagle.get('version') #TODO: warn if absent
        self.note    = list()
        self.drawing = None
        for compatibility in eagle.findall('compatibility'):
            for n in compatibility.findall('note'):
                self.note.append(Note(n))
        for d in eagle.findall('drawing'): #TODO: warn if multiples
            self.drawing = Drawing(d)


class Note:
    def __init__(self, note):
        self.version  = note.get("version")  #TODO: warn if absent
        self.severity = note.get("severity") #TODO: warn if absent
        

class Drawing:
    def __init__(self, drawing):
        self.setting    = list()
        self.layer      = list()
        self.grid       = None
        self.schematic  = None
        for settings in drawing.findall('settings'):
            for s in settings.findall('settings'):
                self.setting.append(Setting(s))
        for g in drawing.findall('grid'): #TODO: warn if multiples
            self.grid = Grid(g)
        for layers in drawing.findall('layers'):
            for l in layers.findall('layer'):
                self.layer.append(Layer(l))
        for s in drawing.findall('schematic'): #TODO: warn if multiples
            self.schematic = Schematic(s)

class Library:
    def __init__(self,library):
        self.description = list()
        self.package     = list()
        self.symbol      = dict()
        self.deviceset   = dict()
        self.name        = library.get("name") #TODO: warn if not present
        #
        for d in library.findall('description'): #TODO: warn if multiples
            self.description = d.text 
        for packages in library.findall('packages'):
            for p in packages.findall('package'):
                self.package.append(Package(p))
        for symbols in library.findall('symbols'):
            for s in symbols.findall('symbol'):
                self.symbol.append(Symbol(s))
        for devicesets in library.findall('devicesets'):
            for d in devicesets.findall('deviceset'):
                self.deviceset.append(Deviceset(d))

class Schematic:
    def __init__(self, schematic):
        self.description = None
        self.library    = list()
        self.attribute  = list()
        self.variantdef = list()
        self.class_     = list() # Python has a cluttered namespace
        self.part       = list()
        self.sheet      = list()
        self.xreflabel  = schematic.get("xreflabel")
        self.xrefpart   = schematic.get("xrefpart")
        # Someone needs to teach CADSoft how to do proper XML plurality
        for d in schematic.findall('description'): #TODO: warn if multiples
            self.description = d.text
        for libraries in schematic.findall('libraries'):
            for l in libraries.findall('library'):
                self.library.append(Library(l))
        for attributes in schematic.findall('attributes'):
            for a in attributes.findall('attribute'):
                self.attribute.append(Attribute(a))
        for variantdefs in schematic.findall('variantdefs'):
            for v in variantdefs.findall('variantdef'):
				self.variantdef.append(Variantdef(v))
        for classes in schematic.findall('classes'):
            for c in classes.findall('class'):
                self.class_.append(Class(c))
        for parts in schematic.findall('parts'):
            for p in parts.findall('part'):
                self.part.append(Part(p))
        for sheets in schematic.findall('sheets'):
            for s in sheets.findall('sheet'):
                self.sheet.append(Sheet(s))
        for errors in schematic.findall('errors'):
            for e in errors.findall('error'):
                self.error.append(Error(e))

class Board:
    def __init__(self, board):
        self.description = None
        self.plain       = None
        self.library     = list()
        self.attribute   = list()
        self.variantdef  = list()
        self.class_      = list()
        self.designrule  = list()
        self.autorouter  = list()
        self.element     = list()
        self.signal      = list()
        self.error       = list()
        #TODO: if this code is needed, then these need to be checked - Austin
        for d in board.findall('description'): #TODO: warn if multiples
            self.description = d.text
        for plain in board.findall('plain'):
            pass
        for libraries in board.findall('libraries'):
            for l in libraries.findall('library'):
                self.library.append(Library(l))
        for attributes in board.findall('attributes'):
            for a in attributes.findall('attribute'):
                self.attribute.append(Attribute(a))
        for variantdefs in board.findall('variantdefs'):
            for v in variantdefs.findall('variantdef'):
				self.variantdef.append(Variantdef(v))
        for classes in board.findall('classes'):
            for c in classes.findall('class'):
                self.class_.append(Class(c))
        for designrules in board.findall('designrules'):
            for d in designrules.findall('designrule'):
                self.designrule.append(Designrule(d))
        for autorouter in board.findall('autorouter'):
            for p in autorouter.findall('pass'):
                self.autorouter.append(Pass(p))
        for elements in board.findall('elements'):
            for e in elements.findall('element'):
                self.element.append(Element(e))
        for signals in board.findall('signals'):
            for s in signals.findall('signal'):
                self.signal.append(Signal(s))
        for errors in board.findall('errors'):
            for e in errors.findall('error'):
                self.error.append(Error(e))

class Sheet:
    def __init__(self, sheet):
        self.description = None
        self.plain       = list()
        self.instance    = list()
        self.bus         = list()
        self.net         = list()
        for d in sheet.findall('description'): #TODO: warn if multiples
            self.description = d.text
        for plain in sheet.findall('plain'):
            pass
        for instances in sheet.findall('instances'):
            for i in instances.findall('instance'):
                self.instance.append(Instance(i))
        for busses in sheet.findall('busses'):
            for b in busses.find('bus'):
                self.bus.append(Bus(b))
        for nets in sheet.findall('nets'):
            for n in nets.findall('net'):
                self.net.append(Net(n))
class Package:
    def __init__(self, package):
        self.description = None
        self.symbol      = list()
        self.name        = package.get("name")
        #TODO: populate the symbols
        for d in package.findall('description'): #TODO: warn if multiples
            self.description = d.text
        for p in package.findall('polygon'):   self.package.append(Polygon(p))
        for w in package.findall('wire'):      self.package.append(Wire(w))
        for t in package.findall('text'):      self.package.append(Text(t))
        for c in package.findall('circle'):    self.package.append(Circle(c))
        for r in package.findall('rectangle'): self.package.append(Rectangle(r))
        for f in package.findall('frame'):     self.package.append(Frame(f))
        for h in package.findall('hole'):      self.package.append(Hole(h))
        for p in package.findall('pad'):       self.package.append(Pad(p))
        for s in package.findall('smd'):       self.package.append(Smd(s))

class Symbol:
    def __init__(self,symbol):
        self.description = None
        self.shape       = list()
        self.name        = symbol.get("name") #TODO: warn if not present
        for d in symbol.findall('description'):
            self.description = d.text
        for p in symbol.findall('polygon'):   self.shape.append(Polygon(p))
        for w in symbol.findall('wire'):      self.shape.append(Wire(w))
        for t in symbol.findall('text'):      self.shape.append(Text(t))
        for p in symbol.findall('pin'):       self.shape.append(Pin(p))
        for c in symbol.findall('circle'):    self.shape.append(Circle(c))
        for r in symbol.findall('rectangle'): self.shape.append(Rectangle(r))
        for f in symbol.findall('frame'):     self.shape.append(Frame(f))

class Deviceset:
    def __init__(self,deviceset):
        self.description = None
        self.gate        = list()
        self.device      = list()
        self.name        = deviceset.get("name") #TODO: warn if not present
        self.prefix      = deviceset.get("prefix") #TODO: warn if not present
        self.uservalue   = deviceset.get("uservalue") #TODO: warn if not present
        for d in deviceset.findall('description'):
            self.description = d.text
        for gates in deviceset.findall('gates'):
            for g in deviceset.findall('gate'):
                self.gate.append(Gate(g))
        for devices in deviceset.findall('devices'):
            for d in deviceset.findall('device'):
                self.device.append(Device(d))

class Device:
    def __init__(self,device):
        self.connect     = list()
        self.technology  = list()
        self.name        = device.get("name") #TODO: warn if not present
        self.package     = device.get("package") #TODO: warn if not present
        for connects in device.findall('connects'):
            for c in connects.findall('connect'):
                self.device.append(Connect(c))
        for technologies in device.findall('technologies'):
            for t in technologies.findall('technology'):
                self.technology.append(Technology(t))

class Bus:
    def __init__(self,bus):
        self.segment    = list()
        self.name       = bus.get("name") #TODO: warn if not present
        for s in bus.findall('segment'):
            self.segment.append(Segment(s))

class Net:
    def __init__(self,net):
        self.segment    = list()
        self.name       = net.get("name") #TODO: warn if not present
        for s in net.findall('segment'):
            self.segment.append(Segment(s))

class Segment:
    def __init__(self, segment):
        self.pinref     = list()
        self.wire       = list()
        self.junction   = list()
        self.label      = list()
        for p in segment.findall('pinref'):
            self.pinref.append(Pinref(p))
        for w in segment.findall('wire'):
            self.wire.append(Wire(w))
        for j in segment.findall('junction'):
            self.junction.append(Junction(j))
        for l in segment.findall('label'):
            self.label.append(Label(l))

class Signal:
    def __init__(self,signal):
        self.contactref     = list()
        self.polygon        = list()
        self.wire           = list()
        self.via            = list()
        self.name           = signal.get("name") #TODO: warn if not present
        self.class_         = signal.get("class") #TODO: warn if not present
        self.airwireshidden = signal.get("airwireshidden") #TODO: warn if not 
        for c in segment.findall('contactref'):
            self.contactref.append(Contactref(c))
        for p in segment.findall('polygon'):
            self.polygon.append(Polygon(p))
        for w in segment.findall('wire'):
            self.wire.append(Wire(w))
        for v in segment.findall('via'):
            self.via.append(Via(v))

class Part:
    def __init__(self, part):
        self.name       = part.get("name") #TODO: warn if not present
        self.library    = part.get("library")
        self.deviceset  = part.get("deviceset")
        self.device     = part.get("device")
        self.value      = part.get("value")
        self.attribute  = list()
        self.variant    = list()
        for a in part.findall('attribute'): 
            self.attribute.append(Attribute(a))
        for v in part.findall('variant'):
            self.variant.append(Variant(v))
