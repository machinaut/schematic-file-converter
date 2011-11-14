#!/usr/bin/env python
from design_attributes import DesignAttributes
from components import Components

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
        self.set_version("0.0.1","Upverter converter")


    def set_version(self, file_version, exporter):
        self.version['file_version'] = file_version
        self.version['exporter'] = exporter


    def add_component_instance(self, component_instance):
        self.component_instances.append(component_instance)


    def add_component(self, library_id, component):
        self.components.add_component(library_id,component)


    def add_net(self, net):
        self.nets.append(net)


    def set_design_attributes(self, design_attributes):
        self.design_attributes = design_attributes


    def json(self):
        return {
            "version" : self.version,
            "nets" : [n.json() for n in self.nets],
            "components" : self.components.json(),
            "component_instances" :
                [i.json() for i in self.component_instances],
            "design_attributes" : self.design_attributes.json()
            }


