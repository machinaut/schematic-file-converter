#!/usr/bin/env python
import random
import shape

class componentInstance:
  def __init__(self, instance_id, library_id):
    self.instance_id = instance_id
    self.library_id = library_id
    self.symbol_index = list()
  
  def get_instance_id(self):
    return self.instance_id


class Component:
  def __init__(self,library_id,name):
    self.library_id = library_id
    self.name = name
    self.attributes = dict()
    self.symbols = list()

  def add_attribute(self, key, value):
    self.attributes[key] = value

  def add_symbol(self, symbol):
    self.symbols.append(symbol.json())

  def json(self):
    return {"symbols": [s.json() for s in self.symbols],
            "attributes": self.attributes,
            "library_id": self.library_id,
            "name": self.name}

class Symbol:
  def __init__(self):
    self.bodies = list()
  
  def add_body(self, body):
    self.bodies.append(body)

  def json(self):
    return [b.json() for b in self.bodies]

class Body:
  def __init__(self):
    self.shapes = list()
    self.pins = list()

  def add_pin(self, pin):
    self.pins.append(pin)

  def add_shape(self, shape):
    self.shape.append(shape)

  def json(self):
    return {"shapes":[s.json() for s in self.shapes],
            "pins"  :[p.json() for p in self.pins]}

class Pin:
  def __init__(self, pin_number, p1, p2, pin_label):
    self.pin_label = pin_label # is a Label
    self.p1 = p1 # is a Point
    self.p2 = p2 # is a Point
    self.pin_number = pin_number

  def json(self):
    return {"pin_number":self.pin_number,
            "p1":self.p1.json(), 
            "p2":self.p2.json(),
            "pin_label":self.pin_label.json()}

class Point: # Simple point, separate from the 'point' in nets
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def json(self):
    return {"x":self.x, "y":self.y}

# Test case
if __name__=='__main__':
  p1 = Point(0,0)
  p2 = Point(10,10)
  pl = shape.Label(6,6,"teeext","left",90)
  mypin = Pin("2", p1, p2, pl)
  print mypin.json()
