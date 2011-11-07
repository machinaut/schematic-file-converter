#!/usr/bin/env python

class Annotation:
  def __init__(self,value,x,y,rotation,visible):
    self.value = value
    self.x = x
    self.y = y
    self.rotation = rotation
    self.visible = visible

  def json(self):
    return {"value" : self.value, "x":self.x, "y":self.y,
            "rotation" : self.rotation, "visible" : self.visible}
