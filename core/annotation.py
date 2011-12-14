#!/usr/bin/env python

from shape import Point


class Annotation:
    """ The Annotation class represents all cases of annotations """

    def __init__(self, value, x, y, rotation, visible):
        self.value = value
        self.x = x
        self.y = y
        self.rotation = rotation
        self.visible = visible


    def bounds(self):
        """ Return the bounding points of an annotation """
        return [Point(self.x - 10, self.y - 10),
                Point(self.x + 10, self.y + 10)]


    def json(self):
        """ Return an annotation as JSON """
        return {
            "value" : self.value, 
            "x":self.x, 
            "y":self.y,
            "rotation" : self.rotation, 
            "visible" : self.visible
            }
