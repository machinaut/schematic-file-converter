import random

class Component:
  def __init__(self):
    self.library_id = ""
    self.name = ""
    self.attributes = dict()
    self.symbols = list()
  def add_attribute(self, key, value):
    self.attributes[key] = value

  def add_symbol(self, symbol):
    self.symbols.append(symbol.get_dict())
  

class Symbol:
  def __init__(self):
    self.bodies = list()
  
 # def add_body(self, 

class Pin:
  def __init__(self, pin_number, p1, p2, pin_label):
    self.label = pin_label.json()
    self.p1 = p1.get_xy_dict()
    self.p2 = p2.get_xy_dict()
    self.pin_number = pin_number

  def json(self):
    ret = dict({"pin_number":self.pin_number, "p1":self.p1, "p2":self.p2})
    return ret

def newPin(pin_number, p1, p2, pin_label):
  return Pin(pin_number, p1, p2, pin_label).json()


class Point:
  def __init__(self, x, y):
    #TODO: This could possibly generate two identical point IDs
    self.point_id = str(random.getrandbits(128))
    self.x = x
    self.y = y
    self.annotations = list()
    self.attributes = dict()
    self.connected_points = list()
    self.connected_components = list()
  
  def get_point_id(self):
    return self.point_id
  
  def add_connected_point(self, connected_point):
    self.connected_points.append(connected_point.get_point_id())
  
  def add_attribute(self, attribute):
    self.attributes.append(attribute)

  def add_annotation(self, annotation):
    self.annotations.append(annotation)

  def json(self):
    ret = dict({"x":self.x, "y":self.y, "annotations":self.annotations, "attributes":self.attributes, "connected points":self.connected_points, "connected components":self.connected_components})
    return ret

  def get_xy_dict(self):
    return dict({"x":self.x, "y":self.y})


if __name__=='__main__':
  d = dict({"rotation": 0.0,  "value": "name",  "visible": "true", "x": 0, "y": 0})
  p1 = Point(0,0)
  p2 = Point(10,10)
  p3 = Point(6,6)
  mypin = Pin("2", p1, p2, p3)
  print mypin.json()
