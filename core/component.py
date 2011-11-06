import json
import random


class component:
  def __init__(self):
    self.library_id = ""
    self.name = ""
    self.attributes = dict({"attributes":dict()})
    self.symbols = dict({"symbols":list()})
  def add_attribute(self, attribute):
    self.attributes.get("attributes").append(attribute)
  def add_symbol(self, symbol):
    self.symbols.get("symbols").append(symbol.get_dict())

class symbol:
  def __init__(self):
    self.bodies = dict({"bodies":list()})
class body:
  def __init__(self):
    self.pins = dict({"attributes":list()})
    self.shapes = dict({"attributes":list()})


class pin:
  def __init__(self, pin_number, p1, p2, pin_label):
    self.label = pin_label.get_dict()
    self.p1 = p1.get_xy_dict()
    self.p2 = p2.get_xy_dict()
    self.pin_number = pin_number

  def get_dict(self):
    ret = dict({"pin_number":self.pin_number, "p1":self.p1, "p2":self.p2})
    return ret
class componentInstance:
  def __init__(self, instance_id, library_id):
    self.instance_id = instance_id
    self.library_id = library_id
    self.symbol_index = list()
  def get_instance_id(self):
    return self.instance_id

class point:
  def __init__(self, x, y):
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

  def get_dict(self):
    ret = dict({"x":self.x, "y":self.y, "annotations":self.annotations, "attributes":self.attributes, "connected points":self.connected_points, "connected components":self.connected_components})
    return ret

  def get_xy_dict(self):
    return dict({"x":self.x, "y":self.y})

if __name__=='__main__':
  #testfile = open('../A-way-to-connect-an-arduino-to-ethernet.upv', 'r')
  #testjson = json.load(testfile)
#  print testjson
  d = dict({"rotation": 0.0,  "value": "name",  "visible": "true", "x": 0, "y": 0})
  p1 = point(0,0)
  p2 = point(10,10)
  p3 = point(6,6)
  mypin = pin(2, p1, p2, p3)
  print mypin.get_dict()
