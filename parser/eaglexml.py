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
        self.layer      = dict()
        self.grid       = None
        self.schematic  = None
        for settings in drawing.findall('settings'):
            for s in settings.findall('settings'):
                self.setting.append(Setting(s))
        for layers in drawing.findall('layers'):
            for l in layers.findall('layer'):
                self.layer[l.get("name")]=Layer(l)
        for g in drawing.findall('grid'): #TODO: warn if multiples
            self.grid = Grid(g)
        for s in drawing.findall('schematic'): #TODO: warn if multiples
            self.schematic = Schematic(s)


class Library:
    def __init__(self,library):
        self.description = None
        self.package     = dict()
        self.symbol      = dict()
        self.deviceset   = list()
        self.name        = library.get("name") #TODO: warn if not present
        #
        for d in library.findall('description'): #TODO: warn if multiples
            self.description = d.text 
        for p in library.findall('packages'):
            for p in packaddges.findall('package'):
                self.package[p.get("name")]=Package(p)
        for symbols in library.findall('symbols'):
            for s in symbols.findall('symbol'):
                self.symbol[s.get("name")]=Symbol(s)
        for devicesets in library.findall('devicesets'):
            for d in devicesets.findall('deviceset'):
                self.deviceset[d.get("name")]=Deviceset(d)

class Schematic:
    def __init__(self, schematic):
        self.description = None
        self.library    = dict()
        self.attribute  = dict()
        self.variantdef = dict()
        self.class_     = dict() # Python has a cluttered namespace
        self.part       = list()
        self.sheet      = list()
        self.xreflabel  = schematic.get("xreflabel")
        self.xrefpart   = schematic.get("xrefpart")
        # Someone needs to teach CADSoft how to do proper XML plurality
        for d in schematic.findall('description'): #TODO: warn if multiples
            self.description = d.text
        for libraries in schematic.findall('libraries'):
            for l in libraries.findall('library'):
                self.library[l.get("name")]=Library(l)
        for attributes in schematic.findall('attributes'):
            for a in attributes.findall('attribute'):
                self.attribute[a.get("name")]=Attribute(a)
        for variantdefs in schematic.findall('variantdefs'):
            for v in variantdefs.findall('variantdef'):
				self.variantdef[v.get("name")]=Variantdef(v)
        for classes in schematic.findall('classes'):
            for c in classes.findall('class'):
                self.class_[c.get("name")]=Class(c)
        for parts in schematic.findall('parts'):
            for p in parts.findall('part'):
                self.part[p.get("name")]=Part(p)
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
        self.library     = dict()
        self.attribute   = dict()
        self.variantdef  = dict()
        self.class_      = dict()
        self.designrule  = None
        self.autorouter  = dict()
        self.element     = dict()
        self.signal      = dict()
        self.error       = dict() #Hash values, not names...
        #TODO: if this code is needed, then these need to be checked - Austin
        for d in board.findall('description'): #TODO: warn if multiples
            self.description = d.text
        for plain in board.findall('plain'):
            pass
        for libraries in board.findall('libraries'):
            for l in libraries.findall('library'):
                self.library[l.get("name")]=Library(l)
        for attributes in board.findall('attributes'):
            for a in attributes.findall('attribute'):
                self.attribute[a.get("name")]=Attribute(a)
        for variantdefs in board.findall('variantdefs'):
            for v in variantdefs.findall('variantdef'):
				self.variantdef[v.get("name")]=Variantdef(v)
        for classes in board.findall('classes'):
            for c in classes.findall('class'):
                self.class_[c.get("name")]=Class(c)
        for d in board.findall('designrules'):
            pass 
        for autorouter in board.findall('autorouter'):
            for p in autorouter.findall('pass'):
                self.autorouter[p.get("name")]=Pass(p)
        for elements in board.findall('elements'):
            for e in elements.findall('element'):
                self.element[e.get("name")]=Element(e)
        for signals in board.findall('signals'):
            for s in signals.findall('signal'):
                self.signal[s.get("name")]=Signal(s)
        for errors in board.findall('errors'):
            for e in errors.findall('approved'):
                self.error[e.get("hash")]=Error(e)

class Sheet:
    def __init__(self, sheet):
        self.description = None
        self.plain       = list()
        self.instance    = list()
        self.bus         = dict()
        self.net         = dict()
        for d in sheet.findall('description'): #TODO: warn if multiples
            self.description = d.text
        for plain in sheet.findall('plain'):
            pass
        for instances in sheet.findall('instances'):
            for i in instances.findall('instance'):
                self.instance.append(Instance(i))
        for busses in sheet.findall('busses'):
            for b in busses.find('bus'):
                self.bus[b.get("name")]=Bus(b)
        for nets in sheet.findall('nets'):
            for n in nets.findall('net'):
                self.net[n.get("name")]=Net(n)

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
        self.gate        = dict()
        self.device      = list()
        self.name        = deviceset.get("name") #TODO: warn if not present
        self.prefix      = deviceset.get("prefix") #TODO: warn if not present
        self.uservalue   = deviceset.get("uservalue") #TODO: warn if not present
        for d in deviceset.findall('description'):
            self.description = d.text
        for gates in deviceset.findall('gates'):
            for g in deviceset.findall('gate'):
                self.gate[g.get("name")]=Gate(g)
        for devices in deviceset.findall('devices'):
            for d in deviceset.findall('device'):
                self.device.append(Device(d))

class Device:
    def __init__(self,device):
        self.connect     = list()
        self.technology  = dict()
        self.name        = device.get("name") 
        self.package     = device.get("package") 
        for connects in device.findall('connects'):
            for c in connects.findall('connect'):
                self.device.append(Connect(c))
        for technologies in device.findall('technologies'):
            for t in technologies.findall('technology'):
                self.technology[t.get("name")]=Technology(t)

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

class Variantdef:
    def __init__(self, variantdef):
        self.name           = variantdef.get("name")

class Variant:
    def __init__(self, variant):
        self.name           = variant.get("name")
        self.populate       = variant.get("populate") #TODO: convert to bool
        self.value          = variant.get("value") #IMPLIED
        self.technology     = variant.get("technology") #IMPLIED

class Gate:
    def __init__(self, gate):
        self.name           = gate.get("name")
        self.symbol         = gate.get("symbol")
        self.x              = gate.get("x")
        self.y              = gate.get("y")
        self.addlevel       = gate.get("addlevel") #TODO: implement defaults
        self.swaplevel      = gate.get("swaplevel") #TODO: implement defaults

class Wire:
    def __init__(self, wire):
        self.x1             = wire.get("x1")
        self.y1             = wire.get("y1")
        self.x2             = wire.get("x2")
        self.y2             = wire.get("y2")
        self.width          = wire.get("width")
        self.layer          = wire.get("layer")
        self.extent         = wire.get("extent")
        self.style          = wire.get("sytle")
        self.curve          = wire.get("curve")
        self.cap            = wire.get("cap")

class Dimension:
    def __init__(self, dimension):
        self.x1             = dimension.get("x1")
        self.y1             = dimension.get("y1")
        self.x2             = dimension.get("x2")
        self.y2             = dimension.get("y2")
        self.x3             = dimension.get("x3")
        self.y3             = dimension.get("y3")
        self.layer          = dimension.get("layer")
        self.dtype          = dimension.get("dtype")

class Text:
    def __init__(self, text):
        self.pcdata         = description.findall('#PCDATA') #TODO:check me!
        self.x              = text.get("x")
        self.y              = text.get("y")
        self.size           = text.get("size")
        self.layer          = text.get("layer")
        self.font           = text.get("font")
        self.ratio          = text.get("ratio")
        self.rot            = text.get("rot")
        self.align          = text.get("align")

class Circle:
    def __init__(self, circle):
        self.x              = circle.get("x")
        self.y              = circle.get("y")
        self.radius         = circle.get("radius")
        self.width          = circle.get("width")
        self.layer          = circle.get("layer")

class Rectangle:
    def __init__(self, rectangle):
        self.x1             = rectangle.get("x1")
        self.y1             = rectangle.get("y1")
        self.x2             = rectangle.get("x2")
        self.y2             = rectangle.get("y2")
        self.layer          = rectangle.get("layer")
        self.rot            = rectangle.get("rot")

class Frame:
    def __init__(self, frame):
        self.x1             = frame.get("x1")
        self.y1             = frame.get("y1")
        self.x2             = frame.get("x2")
        self.y2             = frame.get("y2")
        self.columns        = frame.get("columns")
        self.rows           = frame.get("rows")
        self.layer          = frame.get("layer")
        self.border_left    = frame.get("border-left")
        self.border_top     = frame.get("border-top")
        self.border_right   = frame.get("border-right")
        self.border_bottom  = frame.get("border-bottom")

class Hole:
    def __init__(self, hole):
        self.x              = hole.get("x")
        self.y              = hole.get("y")
        self.drill          = hole.get("drill")

class Pad:
    def __init__(self, pad):
        self.name           = pad.get("name")
        self.x              = pad.get("x")
        self.y              = pad.get("y")
        self.drill          = pad.get("drill")
        self.diameter       = pad.get("diameter")
        self.shape          = pad.get("shape")
        self.rot            = pad.get("rot")
        self.stop           = pad.get("stop")
        self.thermals       = pad.get("thermals")
        self.first          = pad.get("first")

class Smd:
    def __init__(self, smd):
        self.name           = smd.get("name")
        self.x              = smd.get("x")
        self.y              = smd.get("y")
        self.dx             = smd.get("dx")
        self.dy             = smd.get("dy")
        self.layer          = smd.get("layer")
        self.roundness      = smd.get("roundness")
        self.rot            = smd.get("rot")
        self.stop           = smd.get("stop")
        self.thermals       = smd.get("thermals")
        self.cream          = smd.get("cream")

class Element:
    def __init__(self, element):
        self.attribute      = list()
        self.variant        = list()
        self.name           = element.get("name")
        self.library        = element.get("library")
        self.package        = element.get("package")
        self.value          = element.get("value")
        self.x              = element.get("x")
        self.y              = element.get("y")
        self.locked         = element.get("locked")
        self.smashed        = element.get("smashed")
        self.rot            = element.get("rot")
        for a in element.findall('attribute'):
            self.attribute.append(Attribute(a))
        for v in element.findall('variant'):
            self.variant.append(Variant(v))

class Via:
    def __init__(self, via):
        self.x              = via.get("x")
        self.y              = via.get("y")
        self.extent         = via.get("extent")
        self.drill          = via.get("drill")
        self.diameter       = via.get("diameter")
        self.shape          = via.get("shape")
        self.alwaysstop     = via.get("alwaysstop")

class Polygon:
    def __init__(self,polygon):
        self.vertex         = list()
        self.width          = polygon.get("width")
        self.layer          = polygon.get("layer")
        self.spacing        = polygon.get("spacing")
        self.pour           = polygon.get("pour")
        self.isolate        = polygon.get("isolate")
        self.orphans        = polygon.get("orphans")
        self.thermals       = polygon.get("thermals")
        self.rank           = polygon.get("rank")
        for v in polygon.findall("vertex"):
            self.vertex.append(Vertex(v))

class Vertex:
    def __init__(self,vertex):
        self.x              = vertex.get("x")
        self.y              = vertex.get("y")
        self.curve          = vertex.get("curve")

class Pin:
    def __init__(self,pin):
        self.name           = pin.get("name")
        self.x              = pin.get("x")
        self.y              = pin.get("y")
        self.visible        = pin.get("visible")
        self.length         = pin.get("length")
        self.direction      = pin.get("direction")
        self.function       = pin.get("function")
        self.swaplevel      = pin.get("swaplevel")
        self.rot            = pin.get("rot")

class Part:
    def __init__(self,part):
        self.attribute      = list()
        self.variant        = list()
        self.name           = part.get("name")
        self.library        = part.get("library")
        self.deviceset      = part.get("deviceset")
        self.device         = part.get("device")
        self.technology     = part.get("technology")
        self.value          = part.get("value")
        for a in part.findall('attribute'):
            self.attribute.append(Attribute(a))
        for v in part.findall('variant'):
            self.variant.append(Variant(v))

class Instance:
    def __init__(self,instance):
        self.attribute      = list()
        self.part           = instance.get("part")
        self.gate           = instance.get("gate")
        self.x              = instance.get("x")
        self.y              = instance.get("y")
        self.smashed        = instance.get("smashed")
        self.rot            = instance.get("rot")
        for a in instance.findall('attribute'):
            self.attribute.append(Attribute(a))

class Label:
    def __init__(self,label):
        self.x              = label.get("x")
        self.y              = label.get("y")
        self.size           = label.get("size")
        self.layer          = label.get("layer")
        self.font           = label.get("font")
        self.ratio          = label.get("ratio")
        self.rot            = label.get("rot")
        self.xref           = label.get("xref")

class Junction:
    def __init__(self,junction):
        self.x              = junction.get("x")
        self.y              = junction.get("y")

class Connect:
    def __init__(self,connect):
        self.gate           = connect.get("gate")
        self.pin            = connect.get("pin")
        self.pad            = connect.get("pad")
        self.route          = connect.get("route")

class Technology:
    def __init__(self,technology):
        self.attribute      = list()
        self.name           = technology.get("name")
        for a in technology.findall('attribute'):
            self.attribute.append(Attribute(a))

class Attribute:
    def __init__(self,attribute):
        self.name           = attribute.get("name")
        self.value          = attribute.get("value")
        self.x              = attribute.get("x")
        self.y              = attribute.get("y")
        self.size           = attribute.get("size")
        self.layer          = attribute.get("layer")
        self.font           = attribute.get("font")
        self.ratio          = attribute.get("ratio")
        self.rot            = attribute.get("rot")
        self.display        = attribute.get("display")
        self.constant       = attribute.get("constant")

class Pinref:
    def __init__(self,pinref):
        self.part           = pinref.get("part")
        self.gate           = pinref.get("gate")
        self.pin            = pinref.get("pin")

class Contactref:
    def __init__(self,contactref):
        self.element        = contactref.get("element")
        self.pad            = contactref.get("pad")
        self.route          = contactref.get("route")

class Setting:
    def __init__(self,setting):
        self.alwaysvectorfont = setting.get("alwaysvectorfont")
        self.verticaltext   = setting.get("verticaltext")

class Grid:
    def __init__(self,grid):
        self.distance       = grid.get("distance")
        self.unitdist       = grid.get("unitdist")
        self.unit           = grid.get("unit")
        self.style          = grid.get("style")
        self.multiple       = grid.get("multiple")
        self.display        = grid.get("display")
        self.altdistance    = grid.get("altdistance")
        self.altunitdist    = grid.get("altunitdist")
        self.altunit        = grid.get("altunit")

class layer:
    def __init__(self,layer):
        self.number         = layer.get("number")
        self.name           = layer.get("name")
        self.color          = layer.get("color")
        self.fill           = layer.get("fill")
        self.visible        = layer.get("visible")
        self.active         = layer.get("active")

class Class:
    def __init__(self,class_):
        self.clearance      = list()
        self.number         = class_.get("number")
        self.name           = class_.get("name")
        self.width          = class_.get("width")
        self.drill          = class_.get("drill")
        for c in class_.findall('clearance'):
            self.clearance.append(Clearance(c))

class Clearance:
    def __init__(self,clearance):
        self.class_         = clearance.get('class')
        self.value          = clearance.get("value")

class Description:
    def __init__(self,description):
        self.pcdata         = description.findall('#PCDATA') #TODO:check me!
        self.language       = description.get("language")

class Param:
    def __init__(self,param):
        self.name           = param.get("name")
        self.value          = param.get("value")

class Pass:
    def __init__(self,pass_):
        self.param          = list()
        self.name           = pass_.get("param")
        self.refer          = pass_.get("refer")
        self.active         = pass_.get("active")
        for p in pass_.findall('param'):
            self.param.append(Param(p))

class Approved:
    def __init__(self,approved):
        self.hash_          = approved.get('hash')

