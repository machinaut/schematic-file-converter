#!/usr/bin/env python


class Design:
    """ The Design class represents the whole schematic, which is also
    the top level of the output format.  The internal structure of this
    class closely matches the JSON output."""

    def __init__(self):
        self.nets = []
        self.components = []
        self.component_instances = []
        self.design_attributes = {}
        self.file_version = {"file_version":"0.0.1",
                        "tool_name":"Upverter converter"}

    def add_component_instance(self, component_instance):
        self.component_instances.append(component_instance)

    def add_component(self, component):
        self.components.append(component)
	
    def add_net(self, net):
        self.nets.append(net)

    def json(self):
        """ prettify design for json outputting """
        return {
                "version" : self.file_version,
                "nets" : [n.json() for n in self.nets],
                "components" : [c.json() for c in self.components],
                "component_instances" : [i.json() for i in self.instances],
				"design_attributes" : self.design_attributes
                }
