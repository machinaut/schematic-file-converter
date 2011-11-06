import json
import random

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
    self.annotations = dict({"annotations":list()})
    self.attributes = dict({"attributes":dict()})
    self.connected_points = dict({"connected points":list()})
    self.connected_components = dict({"connected components":list()})
  def get_point_id(self)
    return self.point_id
  
  def add_connected_point(self, connected_point)
    self.connected_points.get("connected points").append(connected_point.get_point_id())
  
  def add_attribute(self, attribute):
    self.attributes.get("attributes").append(attribute)

  def add_annotation(self, annotation):
    self.annotations.get("annotations").append(annotation)

class net:
  def __init__(self, net_id):
    self.net_id = net_id
    self.point_list = list()
    self.annotations = dict({"annotations":list()})
    self.attributes = dict({"attributes":dict()})
    self.points = dict({"points":list()})
   
  def add_attribute(self, attribute):
    self.attributes.get("attributes").append(attribute)

  def add_annotation(self, annotation):
    self.annotations.get("annotations").append(annotation)

  def add_point(self, point):
    self.points.get("points").append(point.get_dict())

if __name__=='__main__':
  test = net(12345)
  print test.annotations.get("annotations")
  testfile = open('../A-way-to-connect-an-arduino-to-ethernet.upv', 'r')
  testjson = json.load(testfile)
#  print testjson
  d = dict({"rotation": 0.0,  "value": "name",  "visible": "true", "x": 0, "y": 0})
  test.add_annotation(d)
  print test.annotations.get("annotations")
  p1 = point(0,0)
  p2 = point(10,10)
  p1.add_connected_point
