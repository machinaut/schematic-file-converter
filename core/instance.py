#!/usr/bin/env python
import random
import shape, annotation

class Instance:
  def __init__(self, instance_id, library_id, symbol_index):
    self.instance_id = instance_id
    self.library_id = library_id
    self.symbol_index = symbol_index
    self.symbol_attributes = list()
    self.attributes = dict()

  def add_attribute(self, key, value):
    self.attributes[key] = value

  def add_symbol_attribute(self,x,y,rotation,annotations):
    sa = SymbolAttribute(x,y,rotation,annotations)
    self.symbol_attributes.append(sa)
  
  def get_instance_id(self):
    return self.instance_id

  def json(self):
    return {"instance_id" : self.instance_id,
            "library_id" : self.library_id,
            "symbol_index" : self.symbol_index,
            "symbol_attributes":[s.json() for s in self.symbol_attributes],
            "attributes" : self.attributes}

class SymbolAttribute:
  def __init__(self,x,y,rotation,annotations):
    self.x = x
    self.y = y
    self.rotation = rotation
    self.annotations = annotations

  def addannotation(self, annotation):
    self.annotations.append(annotation)

  def json(self):
    return {"x" : x, "y": y, "rotation":rotation,
            "annotations":[a.json() for a in self.annotations]}

if __name__ == "__main__":
  pass
