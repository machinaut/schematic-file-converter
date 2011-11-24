#!/usr/bin/env python

class Annotation:
    """ The Annotation class represents all cases of annotations """

    def __init__(self,value,x,y,rotation,visible):
        self.value = value
        self.x = x
        self.y = y
        self.rotation = rotation
        self.visible = visible

    def bounds(self):
        return (self.x - 10, self.y - 10, self.x + 10, self.y + 10)

    def json(self):
        return {
            "value" : self.value,
            "x":self.x,
            "y":self.y,
            "rotation" : self.rotation,
            "visible" : self.visible
            }
