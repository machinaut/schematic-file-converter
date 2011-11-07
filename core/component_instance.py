#!/usr/bin/env python

class ComponentInstance:
    """ An instance of a component with a specific symbol """

    def __init__(self, instance_id, library_id, symbol_index):
        self.instance_id = instance_id
        self.library_id = library_id
        self.symbol_index = symbol_index
        self.symbol_attributes = list()
        self.attributes = dict()


    def add_attribute(self, attribute):
        self.attributes[attribute.key] = attribute.value


    def add_symbol_attribute(self,symbol_attribute):
        self.symbol_attributes.append(symbol_attribute)


    def get_instance_id(self):
        return self.instance_id


    def json(self):
        return {
            "instance_id" : self.instance_id,
            "library_id" : self.library_id,
            "symbol_index" : self.symbol_index,
            "symbol_attributes":[s.json() for s in self.symbol_attributes],
            "attributes" : self.attributes
            }


class SymbolAttribute:
    """ The instance of a single body.  There should be a SymbolAttribute
    for every body in the symbol that ComponentInstance is an instance of
    """

    def __init__(self,x,y,rotation):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.annotations = []


    def add_annotation(self, annotation):
        self.annotations.append(annotation)


    def json(self):
        return {
            "x" : self.x,
            "y": self.y,
            "rotation":self.rotation,
            "annotations" : [a.json() for a in self.annotations]
            }
