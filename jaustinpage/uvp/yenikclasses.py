import json

class componentInstance:
  def __init__(self, instance_id, library_id):
    self.instance_id = instance_id
    self.library_id = library_id
    self.symbol_index = list()


class net:
  def __init__(self, net_id):
    self.net_id = net_id
    self.point_list = list()
    self.annotations = dict({"annotations":[]})
    self.attributes = dict({"attributes":dict()})
    self.points = dict({"points":[]})
   
  def add_attribute(self, attribute):
    self.attributes
  def add_annotation(self, annotation):
    self.annotations["annotation"].append(annotation)
    
if __name__=='__main__':
  test = net(12345)
  print test.annotations["annotations"][0]["value"]
  testfile = open('../A-way-to-connect-an-arduino-to-ethernet.upv', 'r')
  testjson = json.load(testfile)
#  print testjson
  
