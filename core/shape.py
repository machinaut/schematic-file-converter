#!/usr/bin/env python

class Shape:
    """a Shape with metadata and a list of shape parts
    Iternal representation of the shapes closely matches JSON shapes """

    def __init__(self):
        self.type = None


class Rectangle(Shape):
    """ A rectangle, defined by x,y of top left corner and width, height"""

    def __init__(self,x,y,width,height):
        self.type = "rectangle"
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    @classmethod
    def fromCorners(cls,x,y,x2,y2):
        """ (x,y) is the top left corner, (x2,y2) is the bottom right """
        width = x2-x
        height = y2-y
        return cls(x,y,width,height)


    def json(self):
        return {
            "height":self.height,
            "type":self.type,
            "width":self.width,
            "x":self.x,
            "y":self.y,
            }


class RoundedRectangle(Shape):

  def __init__(self,x,y,width,height,radius):
    """ x and y are from the top left corner of the rectangle """
    self.type = "rounded_rectangle"
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.radius = radius
  @classmethod
  def fromCorners(cls,x,y,x2,y2,radius):
    """ x and y are the top left corner of the rectangle, x2 and y2 are the
    bottom right corner of the rectangle """
    x = x
    y = y
    width = x2-x
    height = y2-y
    radius = radius
    return cls(x,y,width,height,radius)
  def json(self):
    """ return a dict for json outputting """
    return {
        "height":self.height,
        "type":self.type,
        "width":self.width,
        "x":self.x,
        "y":self.y,
        "radius":self.radius,
        }

class Arc(Shape):

  def __init__(self,x,y,start_angle,end_angle,radius):
    self.type = "arc"
    self.x = x
    self.y = y
    self.start_angle = start_angle
    self.end_angle = end_angle
    self.radius = radius
  def json(self):
    """ return a dict for json outputting """
    return {
        "start_angle":self.start_angle,
        "end_angle":self.end_angle,
        "type":self.type,
        "radius":self.radius,
        "x":self.x,
        "y":self.y,
        }

class Circle(Shape):
    """ circle defined by center point x,y and radius """

    def __init__(self,x,y,radius):
        self.type = "circle"
        self.x = x
        self.y = y
        self.radius = radius


    def json(self):
        """ return a dict for json outputting """
        return {
            "radius":self.radius,
            "type":self.type,
            "x":self.x,
            "y":self.y,
            }


class Label(Shape):
    """ Text label with x,y location, alignment, rotation and text.
    Alignment can be 'left','right', or 'center'.
    """

    def __init__(self,x,y,text,align,rotation):
        self.type = "label"
        self.x = x
        self.y = y
        self.text = text
        self.rotation = rotation # TODO verify correct value
        # Parse , TODO maybe clean this up some, dont need to accept
        #   all of these inputs, converting to lowercase would be enough
        if align in ["left","Left"]:
            self.align = "left"
        elif align in ["right","Right"]:
            self.align = "right"
        elif align in ["center", "Center", "centered","Centered","middle"]:
            self.align = "center"
        else:
            raise ValueError("Label requires the align to be either " +
                    "\"left\", \"right\", or \"center\" ")


    def json(self):
        return {
            "type":self.type,
            "align":self.align,
            "rotation":self.rotation,
            "text":self.text,
            "x":self.x,
            "y":self.y,
            }


class Line(Shape):
    """ line segment from point1 to point2 """

    def __init__(self,p1,p2):
        self.type = "line"
        self.p1 = Point(p1)
        self.p2 = Point(p2)


    def json(self):
        """ return a dict for json outputting """
        return {
            "type":self.type,
            "p1":self.p1.json(),
            "p2":self.p2.json(),
            }


class Polygon(Shape):
    """ A polygon is just a list of points, drawn as connected in order """

    def __init__(self):
        self.type = "polygon"
        self.points = list()


    def addPoint(self, x, y=None):
        self.points.append(Point(x, y))


    def json(self):
        return {
            "type":self.type,
            "points":[p.json() for p in self.points],
            }


class BezierCurve(Shape):
    """ A parametric curved line """

    def __init__(self,control1,control2,p1,p2):
        self.type = "bezier"
        self.control1 = Point(control1)
        self.control2 = Point(control2)
        self.p1 = Point(p1)
        self.p2 = Point(p2)


    def build(self,control1x,control1y,control2x,control2y,p1x,
            p1y,p2x,p2y):
        self.type = "bezier"
        self.control1 = {"x":control1x,"y":control1y}
        self.control2 = {"x":control2x,"y":control2y}
        self.p1 = {"x":p1x,"y":p1y}
        self.p2 = {"x":p2x,"y":p2y}


    def json(self):
        """ return a dict for json outputting """
        return {
            "type":self.type,
            "control1":self.control1.json(),
            "control2":self.control2.json(),
            "p1":self.p1.json(),
            "p2":self.p2.json(),
            }


class Point:
    """ Simple x,y coordinate. Different from the 'Point' in Nets """

    def __init__(self, x, y=None):
        if y is not None:
            self.x = x
            self.y = y
        # Do a copy of a Point if passed
        elif isinstance(x, Point):
            self.x = x.x
            self.y = x.y
        # Allow for instantiation from a tuple
        else:
            self.x, self.y = x


    def json(self):
        return {
            "x":self.x,
            "y":self.y
            }

