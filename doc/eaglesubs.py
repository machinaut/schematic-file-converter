#!/usr/bin/env python

#
# Generated Wed Nov  9 18:31:45 2011 by generateDS.py version 2.7a.
#

import sys

import ??? as supermod

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#

class eagleSub(supermod.eagle):
    def __init__(self, version=None, compatibility=None, drawing=None):
        super(eagleSub, self).__init__(version, compatibility, drawing, )
supermod.eagle.subclass = eagleSub
# end class eagleSub


class compatibilitySub(supermod.compatibility):
    def __init__(self, note=None):
        super(compatibilitySub, self).__init__(note, )
supermod.compatibility.subclass = compatibilitySub
# end class compatibilitySub


class noteSub(supermod.note):
    def __init__(self, version=None, severity=None, valueOf_=None, mixedclass_=None, content_=None):
        super(noteSub, self).__init__(version, severity, valueOf_, mixedclass_, content_, )
supermod.note.subclass = noteSub
# end class noteSub


class drawingSub(supermod.drawing):
    def __init__(self, settings=None, grid=None, layers=None, library=None, schematic=None, board=None):
        super(drawingSub, self).__init__(settings, grid, layers, library, schematic, board, )
supermod.drawing.subclass = drawingSub
# end class drawingSub


class librarySub(supermod.library):
    def __init__(self, name=None, description=None, packages=None, symbols=None, devicesets=None):
        super(librarySub, self).__init__(name, description, packages, symbols, devicesets, )
supermod.library.subclass = librarySub
# end class librarySub


class schematicSub(supermod.schematic):
    def __init__(self, xrefpart=None, xreflabel=None, description=None, libraries=None, attributes=None, variantdefs=None, classes=None, parts=None, sheets=None, errors=None):
        super(schematicSub, self).__init__(xrefpart, xreflabel, description, libraries, attributes, variantdefs, classes, parts, sheets, errors, )
supermod.schematic.subclass = schematicSub
# end class schematicSub


class boardSub(supermod.board):
    def __init__(self, description=None, plain=None, libraries=None, attributes=None, variantdefs=None, classes=None, designrules=None, autorouter=None, elements=None, signals=None, errors=None):
        super(boardSub, self).__init__(description, plain, libraries, attributes, variantdefs, classes, designrules, autorouter, elements, signals, errors, )
supermod.board.subclass = boardSub
# end class boardSub


class sheetSub(supermod.sheet):
    def __init__(self, description=None, plain=None, instances=None, busses=None, nets=None):
        super(sheetSub, self).__init__(description, plain, instances, busses, nets, )
supermod.sheet.subclass = sheetSub
# end class sheetSub


class packageSub(supermod.package):
    def __init__(self, name=None, description=None, polygon=None, wire=None, text=None, circle=None, rectangle=None, frame=None, hole=None, pad=None, smd=None):
        super(packageSub, self).__init__(name, description, polygon, wire, text, circle, rectangle, frame, hole, pad, smd, )
supermod.package.subclass = packageSub
# end class packageSub


class symbolSub(supermod.symbol):
    def __init__(self, name=None, description=None, polygon=None, wire=None, text=None, pin=None, circle=None, rectangle=None, frame=None):
        super(symbolSub, self).__init__(name, description, polygon, wire, text, pin, circle, rectangle, frame, )
supermod.symbol.subclass = symbolSub
# end class symbolSub


class devicesetSub(supermod.deviceset):
    def __init__(self, uservalue=None, prefix=None, name=None, description=None, gates=None, devices=None):
        super(devicesetSub, self).__init__(uservalue, prefix, name, description, gates, devices, )
supermod.deviceset.subclass = devicesetSub
# end class devicesetSub


class deviceSub(supermod.device):
    def __init__(self, name=None, package=None, connects=None, technologies=None):
        super(deviceSub, self).__init__(name, package, connects, technologies, )
supermod.device.subclass = deviceSub
# end class deviceSub


class busSub(supermod.bus):
    def __init__(self, name=None, segment=None):
        super(busSub, self).__init__(name, segment, )
supermod.bus.subclass = busSub
# end class busSub


class netSub(supermod.net):
    def __init__(self, name=None, classxx=None, segment=None):
        super(netSub, self).__init__(name, classxx, segment, )
supermod.net.subclass = netSub
# end class netSub


class segmentSub(supermod.segment):
    def __init__(self, pinref=None, wire=None, junction=None, label=None):
        super(segmentSub, self).__init__(pinref, wire, junction, label, )
supermod.segment.subclass = segmentSub
# end class segmentSub


class signalSub(supermod.signal):
    def __init__(self, airwireshidden=None, name=None, classxx=None, contactref=None, polygon=None, wire=None, via=None):
        super(signalSub, self).__init__(airwireshidden, name, classxx, contactref, polygon, wire, via, )
supermod.signal.subclass = signalSub
# end class signalSub


class variantdefSub(supermod.variantdef):
    def __init__(self, name=None):
        super(variantdefSub, self).__init__(name, )
supermod.variantdef.subclass = variantdefSub
# end class variantdefSub


class variantSub(supermod.variant):
    def __init__(self, value=None, technology=None, name=None, populate=None):
        super(variantSub, self).__init__(value, technology, name, populate, )
supermod.variant.subclass = variantSub
# end class variantSub


class gateSub(supermod.gate):
    def __init__(self, name=None, symbol=None, swaplevel=None, addlevel=None, y=None, x=None):
        super(gateSub, self).__init__(name, symbol, swaplevel, addlevel, y, x, )
supermod.gate.subclass = gateSub
# end class gateSub


class wireSub(supermod.wire):
    def __init__(self, layer=None, y2=None, width=None, cap=None, curve=None, style=None, x2=None, extent=None, y1=None, x1=None):
        super(wireSub, self).__init__(layer, y2, width, cap, curve, style, x2, extent, y1, x1, )
supermod.wire.subclass = wireSub
# end class wireSub


class dimensionSub(supermod.dimension):
    def __init__(self, layer=None, y2=None, dtype=None, x2=None, y1=None, x3=None, y3=None, x1=None):
        super(dimensionSub, self).__init__(layer, y2, dtype, x2, y1, x3, y3, x1, )
supermod.dimension.subclass = dimensionSub
# end class dimensionSub


class textSub(supermod.text):
    def __init__(self, layer=None, ratio=None, align=None, y=None, x=None, font=None, rot=None, size=None, valueOf_=None, mixedclass_=None, content_=None):
        super(textSub, self).__init__(layer, ratio, align, y, x, font, rot, size, valueOf_, mixedclass_, content_, )
supermod.text.subclass = textSub
# end class textSub


class circleSub(supermod.circle):
    def __init__(self, y=None, x=None, layer=None, radius=None, width=None):
        super(circleSub, self).__init__(y, x, layer, radius, width, )
supermod.circle.subclass = circleSub
# end class circleSub


class rectangleSub(supermod.rectangle):
    def __init__(self, layer=None, y2=None, x2=None, y1=None, x1=None, rot=None):
        super(rectangleSub, self).__init__(layer, y2, x2, y1, x1, rot, )
supermod.rectangle.subclass = rectangleSub
# end class rectangleSub


class frameSub(supermod.frame):
    def __init__(self, y2=None, layer=None, rows=None, border_right=None, border_bottom=None, x2=None, border_top=None, border_left=None, y1=None, x1=None, columns=None):
        super(frameSub, self).__init__(y2, layer, rows, border_right, border_bottom, x2, border_top, border_left, y1, x1, columns, )
supermod.frame.subclass = frameSub
# end class frameSub


class holeSub(supermod.hole):
    def __init__(self, y=None, x=None, drill=None):
        super(holeSub, self).__init__(y, x, drill, )
supermod.hole.subclass = holeSub
# end class holeSub


class padSub(supermod.pad):
    def __init__(self, diameter=None, thermals=None, name=None, stop=None, shape=None, drill=None, y=None, x=None, rot=None, first=None):
        super(padSub, self).__init__(diameter, thermals, name, stop, shape, drill, y, x, rot, first, )
supermod.pad.subclass = padSub
# end class padSub


class smdSub(supermod.smd):
    def __init__(self, layer=None, thermals=None, name=None, stop=None, roundness=None, dx=None, dy=None, y=None, x=None, rot=None, cream=None):
        super(smdSub, self).__init__(layer, thermals, name, stop, roundness, dx, dy, y, x, rot, cream, )
supermod.smd.subclass = smdSub
# end class smdSub


class elementSub(supermod.element):
    def __init__(self, locked=None, name=None, package=None, value=None, smashed=None, library=None, y=None, x=None, rot=None, attribute=None, variant=None):
        super(elementSub, self).__init__(locked, name, package, value, smashed, library, y, x, rot, attribute, variant, )
supermod.element.subclass = elementSub
# end class elementSub


class viaSub(supermod.via):
    def __init__(self, diameter=None, extent=None, shape=None, alwaysstop=None, drill=None, y=None, x=None):
        super(viaSub, self).__init__(diameter, extent, shape, alwaysstop, drill, y, x, )
supermod.via.subclass = viaSub
# end class viaSub


class polygonSub(supermod.polygon):
    def __init__(self, layer=None, thermals=None, spacing=None, orphans=None, isolate=None, pour=None, width=None, rank=None, vertex=None):
        super(polygonSub, self).__init__(layer, thermals, spacing, orphans, isolate, pour, width, rank, vertex, )
supermod.polygon.subclass = polygonSub
# end class polygonSub


class vertexSub(supermod.vertex):
    def __init__(self, y=None, x=None, curve=None):
        super(vertexSub, self).__init__(y, x, curve, )
supermod.vertex.subclass = vertexSub
# end class vertexSub


class pinSub(supermod.pin):
    def __init__(self, function=None, direction=None, name=None, visible=None, length=None, y=None, x=None, rot=None, swaplevel=None):
        super(pinSub, self).__init__(function, direction, name, visible, length, y, x, rot, swaplevel, )
supermod.pin.subclass = pinSub
# end class pinSub


class partSub(supermod.part):
    def __init__(self, name=None, deviceset=None, value=None, library=None, device=None, technology=None, attribute=None, variant=None):
        super(partSub, self).__init__(name, deviceset, value, library, device, technology, attribute, variant, )
supermod.part.subclass = partSub
# end class partSub


class instanceSub(supermod.instance):
    def __init__(self, smashed=None, part=None, x=None, y=None, gate=None, rot=None, attribute=None):
        super(instanceSub, self).__init__(smashed, part, x, y, gate, rot, attribute, )
supermod.instance.subclass = instanceSub
# end class instanceSub


class labelSub(supermod.label):
    def __init__(self, layer=None, xref=None, ratio=None, y=None, x=None, font=None, rot=None, size=None):
        super(labelSub, self).__init__(layer, xref, ratio, y, x, font, rot, size, )
supermod.label.subclass = labelSub
# end class labelSub


class junctionSub(supermod.junction):
    def __init__(self, y=None, x=None):
        super(junctionSub, self).__init__(y, x, )
supermod.junction.subclass = junctionSub
# end class junctionSub


class connectSub(supermod.connect):
    def __init__(self, gate=None, route=None, pad=None, pin=None):
        super(connectSub, self).__init__(gate, route, pad, pin, )
supermod.connect.subclass = connectSub
# end class connectSub


class technologySub(supermod.technology):
    def __init__(self, name=None, attribute=None):
        super(technologySub, self).__init__(name, attribute, )
supermod.technology.subclass = technologySub
# end class technologySub


class attributeSub(supermod.attribute):
    def __init__(self, layer=None, ratio=None, name=None, value=None, y=None, x=None, constant=None, font=None, rot=None, display=None, size=None):
        super(attributeSub, self).__init__(layer, ratio, name, value, y, x, constant, font, rot, display, size, )
supermod.attribute.subclass = attributeSub
# end class attributeSub


class pinrefSub(supermod.pinref):
    def __init__(self, gate=None, part=None, pin=None):
        super(pinrefSub, self).__init__(gate, part, pin, )
supermod.pinref.subclass = pinrefSub
# end class pinrefSub


class contactrefSub(supermod.contactref):
    def __init__(self, route=None, pad=None, element=None):
        super(contactrefSub, self).__init__(route, pad, element, )
supermod.contactref.subclass = contactrefSub
# end class contactrefSub


class variantdefsSub(supermod.variantdefs):
    def __init__(self, variantdef=None):
        super(variantdefsSub, self).__init__(variantdef, )
supermod.variantdefs.subclass = variantdefsSub
# end class variantdefsSub


class settingsSub(supermod.settings):
    def __init__(self, setting=None):
        super(settingsSub, self).__init__(setting, )
supermod.settings.subclass = settingsSub
# end class settingsSub


class sheetsSub(supermod.sheets):
    def __init__(self, sheet=None):
        super(sheetsSub, self).__init__(sheet, )
supermod.sheets.subclass = sheetsSub
# end class sheetsSub


class layersSub(supermod.layers):
    def __init__(self, layer=None):
        super(layersSub, self).__init__(layer, )
supermod.layers.subclass = layersSub
# end class layersSub


class packagesSub(supermod.packages):
    def __init__(self, package=None):
        super(packagesSub, self).__init__(package, )
supermod.packages.subclass = packagesSub
# end class packagesSub


class symbolsSub(supermod.symbols):
    def __init__(self, symbol=None):
        super(symbolsSub, self).__init__(symbol, )
supermod.symbols.subclass = symbolsSub
# end class symbolsSub


class devicesetsSub(supermod.devicesets):
    def __init__(self, deviceset=None):
        super(devicesetsSub, self).__init__(deviceset, )
supermod.devicesets.subclass = devicesetsSub
# end class devicesetsSub


class gatesSub(supermod.gates):
    def __init__(self, gate=None):
        super(gatesSub, self).__init__(gate, )
supermod.gates.subclass = gatesSub
# end class gatesSub


class devicesSub(supermod.devices):
    def __init__(self, device=None):
        super(devicesSub, self).__init__(device, )
supermod.devices.subclass = devicesSub
# end class devicesSub


class librariesSub(supermod.libraries):
    def __init__(self, library=None):
        super(librariesSub, self).__init__(library, )
supermod.libraries.subclass = librariesSub
# end class librariesSub


class connectsSub(supermod.connects):
    def __init__(self, connect=None):
        super(connectsSub, self).__init__(connect, )
supermod.connects.subclass = connectsSub
# end class connectsSub


class technologiesSub(supermod.technologies):
    def __init__(self, technology=None):
        super(technologiesSub, self).__init__(technology, )
supermod.technologies.subclass = technologiesSub
# end class technologiesSub


class attributesSub(supermod.attributes):
    def __init__(self, attribute=None):
        super(attributesSub, self).__init__(attribute, )
supermod.attributes.subclass = attributesSub
# end class attributesSub


class classesSub(supermod.classes):
    def __init__(self, classxx=None):
        super(classesSub, self).__init__(classxx, )
supermod.classes.subclass = classesSub
# end class classesSub


class partsSub(supermod.parts):
    def __init__(self, part=None):
        super(partsSub, self).__init__(part, )
supermod.parts.subclass = partsSub
# end class partsSub


class instancesSub(supermod.instances):
    def __init__(self, instance=None):
        super(instancesSub, self).__init__(instance, )
supermod.instances.subclass = instancesSub
# end class instancesSub


class errorsSub(supermod.errors):
    def __init__(self, approved=None):
        super(errorsSub, self).__init__(approved, )
supermod.errors.subclass = errorsSub
# end class errorsSub


class plainSub(supermod.plain):
    def __init__(self, polygon=None, wire=None, text=None, circle=None, rectangle=None, frame=None, hole=None):
        super(plainSub, self).__init__(polygon, wire, text, circle, rectangle, frame, hole, )
supermod.plain.subclass = plainSub
# end class plainSub


class designrulesSub(supermod.designrules):
    def __init__(self, description=None, param=None):
        super(designrulesSub, self).__init__(description, param, )
supermod.designrules.subclass = designrulesSub
# end class designrulesSub


class autorouterSub(supermod.autorouter):
    def __init__(self, passxx=None):
        super(autorouterSub, self).__init__(passxx, )
supermod.autorouter.subclass = autorouterSub
# end class autorouterSub


class elementsSub(supermod.elements):
    def __init__(self, element=None):
        super(elementsSub, self).__init__(element, )
supermod.elements.subclass = elementsSub
# end class elementsSub


class signalsSub(supermod.signals):
    def __init__(self, signal=None):
        super(signalsSub, self).__init__(signal, )
supermod.signals.subclass = signalsSub
# end class signalsSub


class bussesSub(supermod.busses):
    def __init__(self, bus=None):
        super(bussesSub, self).__init__(bus, )
supermod.busses.subclass = bussesSub
# end class bussesSub


class netsSub(supermod.nets):
    def __init__(self, net=None):
        super(netsSub, self).__init__(net, )
supermod.nets.subclass = netsSub
# end class netsSub


class settingSub(supermod.setting):
    def __init__(self, alwaysvectorfont=None, verticaltext=None):
        super(settingSub, self).__init__(alwaysvectorfont, verticaltext, )
supermod.setting.subclass = settingSub
# end class settingSub


class gridSub(supermod.grid):
    def __init__(self, distance=None, style=None, multiple=None, altdistance=None, altunit=None, unitdist=None, altunitdist=None, display=None, unit=None):
        super(gridSub, self).__init__(distance, style, multiple, altdistance, altunit, unitdist, altunitdist, display, unit, )
supermod.grid.subclass = gridSub
# end class gridSub


class layerSub(supermod.layer):
    def __init__(self, name=None, color=None, number=None, visible=None, active=None, fill=None):
        super(layerSub, self).__init__(name, color, number, visible, active, fill, )
supermod.layer.subclass = layerSub
# end class layerSub


class classxxSub(supermod.classxx):
    def __init__(self, width=None, number=None, drill=None, name=None, clearance=None):
        super(classxxSub, self).__init__(width, number, drill, name, clearance, )
supermod.classxx.subclass = classxxSub
# end class classxxSub


class clearanceSub(supermod.clearance):
    def __init__(self, classxx=None, value=None):
        super(clearanceSub, self).__init__(classxx, value, )
supermod.clearance.subclass = clearanceSub
# end class clearanceSub


class descriptionSub(supermod.description):
    def __init__(self, language=None, valueOf_=None, mixedclass_=None, content_=None):
        super(descriptionSub, self).__init__(language, valueOf_, mixedclass_, content_, )
supermod.description.subclass = descriptionSub
# end class descriptionSub


class paramSub(supermod.param):
    def __init__(self, name=None, value=None):
        super(paramSub, self).__init__(name, value, )
supermod.param.subclass = paramSub
# end class paramSub


class passxxSub(supermod.passxx):
    def __init__(self, active=None, name=None, refer=None, param=None):
        super(passxxSub, self).__init__(active, name, refer, param, )
supermod.passxx.subclass = passxxSub
# end class passxxSub


class approvedSub(supermod.approved):
    def __init__(self, hash=None):
        super(approvedSub, self).__init__(hash, )
supermod.approved.subclass = approvedSub
# end class approvedSub



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    if hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eagle'
        rootClass = supermod.eagle
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    doc = None
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eagle'
        rootClass = supermod.eagle
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eagle'
        rootClass = supermod.eagle
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from ??? import *\n\n')
    sys.stdout.write('import ??? as model_\n\n')
    sys.stdout.write('rootObj = model_.eagle(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="eagle")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


