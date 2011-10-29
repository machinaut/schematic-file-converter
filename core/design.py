#!/usr/bin/env python


class Design:
    """ Design represents the whole schematic, and the top level of the output format
    Internal representation of a Design, closely matches JSON Design"""

    def __init__(self):
        self.version = {"file_version":"0.0.1", "tool_name":"Upverter converter"}
        self.nets = []
        self.components = []
        self.instances = []
        self.attributes = []


    def json(self):
        """ prettify design for json outputting """
        return {
                "version" : self.version,
                "nets" : [i.json() for i in self.nets],
                "components" : self.components,
                "instances" : self.instances,
                "attributes" : self.attributes
                }
