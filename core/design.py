#!/usr/bin/env python


class Design:
    """ Design represents the whole schematic, and the top level of the output format
    Internal representation of a Design, closely matches JSON Design"""

    def __init__(self):
        self.version = {"file_version":"0.0.1", "tool_name":"Upverter converter"}
        self.nets = []
        self.components = []
        self.instances = []
        self.attributes = {}

    def add_instance(self, instance):
        self.instances.append(instance)

    def add_component(self, component):
        self.components.append(component)
	
	def add_net(self, net):
		self.nets.append(net)

	def add_attribute(self, key, value):
		self.attributes[key] = value

    def json(self):
        """ prettify design for json outputting """
        return {
                "version" : self.version,
                "nets" : [n.json() for n in self.nets],
                "components" : [c.json() for c in self.components],
                "component_instances" : [i.json() for i in self.instances],
                "design_attributes": {
                  "annotations": [], 
                  "attributes": {
                    "_resistor_counter": "1", 
                  },  
                  "metadata": {
                    "attached_urls": [
                      "http://google.com/"
                    ], 
                    "description": "test file",
                    "design_id": "0000000000001337", 
                    "license": "", 
                    "name": "My Test", 
                    "owner": "Alex", 
                    "slug": "Test", 
                    "updated_timestamp": 1234567890
                  }
                }
                }
