#!/usr/bin/env python
import random
import shape

class Component:
    """ The Component class represents a single kind of part (component).
    It can have multiple graphical representations (Symbols), each with 
    multiple sections (Bodies).
    The 'components' of a design is basically it's library of available
    parts.  The actual placed parts on the design are 'Instances' of
    components, and reference their respective component via a unique
    library_id.
    """

    def __init__(self,library_id,name):
        self.library_id = library_id
        self.name = name
        self.attributes = dict()
        self.symbols = list()


    def add_attribute(self, key, value):
        self.attributes[key] = value


    def add_symbol(self, symbol):
        self.symbols.append(symbol)


    def json(self):
        return {
            "symbols": [s.json() for s in self.symbols],
            "attributes": self.attributes,
            "library_id": self.library_id,
            "name": self.name
            }


class Symbol:
    """ This is a graphical representation of a Component.
    A Component can have many Symbols, and each Symbol can have
    multiple Bodies """

    def __init__(self):
        self.bodies = list()
  

    def add_body(self, body):
        self.bodies.append(body)


    def json(self):
        return [b.json() for b in self.bodies]


class Body:
    """ A body of a Symbol of a Component """

    def __init__(self):
        self.shapes = list()
        self.pins = list()


    def add_pin(self, pin):
        self.pins.append(pin)


    def add_shape(self, shape):
        self.shapes.append(shape)


    def json(self):
        return {
            "shapes":[s.json() for s in self.shapes],
            "pins"  :[p.json() for p in self.pins]
            }


class Pin:
    """ Pins are the parts of Bodies (/symbols/components) that connect
    to nets. Basically a line segment, with a null end and a connect end
    """

    def __init__(self, pin_number, p1, p2, pin_label):
        self.pin_label = pin_label # is a Label
        self.p1 = p1 # is a Point, null end
        self.p2 = p2 # is a Point, connect end
        self.pin_number = pin_number


    def json(self):
        return {
            "pin_number":self.pin_number,
            "p1":self.p1.json(), 
            "p2":self.p2.json(),
            "pin_label":self.pin_label.json()
            }


class Point:
    """ Simple x,y coordinate. Different from the 'Point' in Nets """

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def json(self):
        return {
            "x":self.x, 
            "y":self.y
            }



