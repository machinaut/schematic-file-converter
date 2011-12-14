#!/usr/bin/env python
from design_attributes import DesignAttributes
from components import Components
from shape import Point

class Design:
    """ The Design class represents the whole schematic, which is also
    the top level of the output format.  The internal structure of this
    class closely matches the JSON output."""

    def __init__(self):
        self.nets = list()
        self.components = Components()
        self.component_instances = list()
        self.design_attributes = DesignAttributes()
        self.version = dict()
<<<<<<< HEAD
        self.set_version("0.1.0","Upverter converter")
=======
        self.set_version("0.0.1", "Upverter converter")


    def bounds(self):
        """ Return the min and max point of a design """
        bounds = [net.bounds() for net in self.nets]
        offset_bounds = lambda (x1, y1, x2, y2), (xo, yo): (x1+xo, y1+yo,
                                                            x2+xo, y2+yo)
        for comp in self.component_instances:
            offsets = [(att.x, att.y) for att in comp.symbol_attributes]
            lib_comp = self.components.components[comp.library_id]
            bbounds = [b.bounds() for b in
                       lib_comp.symbols[comp.symbol_index].bodies]
            bounds.extend([offset_bounds(b, o) for b, o in zip(bbounds, offsets)])
            xs = sum([list(b[0::2]) for b in bounds], [])
            ys = sum([list(b[1::2]) for b in bounds], [])
        return [Point(min(xs), min(ys)), Point(max(xs), max(ys))]
>>>>>>> 5abb89ac932f010195dea31c734cf01a4d7fff5f


    def set_version(self, file_version, exporter):
        """ Set the file version and exporter """
        self.version['file_version'] = file_version
        self.version['exporter'] = exporter


    def add_component_instance(self, component_instance):
        """ Add an instance """
        self.component_instances.append(component_instance)


    def add_component(self, library_id, component):
        """ Add a library part """
        self.components.add_component(library_id, component)


    def add_net(self, net):
        """ Add a net """
        self.nets.append(net)


    def set_design_attributes(self, design_attributes):
        """ Add design level attributes """
        self.design_attributes = design_attributes


    def json(self):
        """ Return a design as JSON """
        return {
            "version" : self.version,
            "nets" : [n.json() for n in self.nets],
            "components" : self.components.json(),
            "component_instances" :
                [i.json() for i in self.component_instances],
            "design_attributes" : self.design_attributes.json()
            }


