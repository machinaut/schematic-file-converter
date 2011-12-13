#!/usr/bin/env python

class Shape:
    """a Shape with metadata and a list of shape parts
    Iternal representation of the shapes closely matches JSON shapes """

    def __init__(self):
        self.type = None
        # All Shapes have a list of Points, self.points. Moving the entire list
        # by a constant (x, y) offset will move the entire shape properly. No
        # promises on rotating yet, no promises on stretching/shearing shapes
        # ever.
        self.points = list()

    def __getattr__(self, name):
        # just here, with __setattr__, for backwards compat. with code that
        # expects theSshape to have shape.x and shape.y
        if name not in ('x', 'y'):
            raise AttributeError("Shape instance has no attribute '%s'" % name)
        return getattr(self.points[0], name)

    def __setattr__(self, name, val):
        if name not in ('x', 'y'):
            self.__dict__[name] = val
        else:
            setattr(self.points[0], name, val)

    def bounds(self):
        ''' returns a 4-tuple (left, top, right, bot) that encloses the 
        entire shape'''
        xs, ys = [p.x for p in self.points], [p.y for p in self.points]
        return (min(xs), min(ys), max(xs), max(ys))

    def translate(self, dx, dy):
        ''' translate (move or slide) the shape by dx and dy '''
        for p in self.points:
            p.x += dx
            p.y += dy

class Rectangle(Shape):
    """ A rectangle, defined by x,y of top left corner and width, height"""

    def __init__(self,x,y,width,height):
        self.type = "rectangle"
        # internally, it's just four Points
        self.points = map(Point, [(x, y), (x+width, y), (x+width, y+height),
                                  (x, y+height)])

    @classmethod
    def fromCorners(cls,x,y,x2,y2):
        """ (x,y) is the top left corner, (x2,y2) is the bottom right """
        width = x2-x
        height = y2-y
        return cls(x,y,width,height)


    def json(self):
        p1, p2 = self.points[:2]
        if p1.x == p2.x or p1.y == p2.y:
            # still lined up along the axes
            (left, top, right, bot) = self.bounds()
            return {
                    "height": bot - top,
                    "type":self.type,
                    "width": right - left,
                    "x":left,
                    "y": top
                    }
        else:
            # in the case that it's been rotated, just treat it like a polygon
            return Polygon(self.points).json()
            # TODO does a closed n-gon need n, or n+1 points?
            # TODO want to set type='rectangle' anyway in the returned dict?


class RoundedRectangle(Rectangle):

    def __init__(self,x,y,width,height,radius):
        """ x and y are from the top left corner of the rectangle """
        Rectangle.__init__(self, x, y, width, height)
        self.type = "rounded_rectangle"
        self.radius = radius

    @classmethod
    def fromCorners(cls,x,y,x2,y2,radius):
        """ x and y are the top left corner of the rectangle, x2 and y2 are the
        bottom right corner of the rectangle """
        width = x2-x
        height = y2-y
        return cls(x,y,width,height,radius)

    def json(self):
        """ return a dict for json outputting """
        ret = Rectangle.json(self)
        ret['radius'] = self.radius
        # will have some weirdness when a rotated RoundedRectangle creates a
        # polygon with a radius value...
        return ret

class Arc(Shape):

    def __init__(self,x,y,start_angle,end_angle,radius):
        self.type = "arc"
        self.points = [Point(x,y)]
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.radius = radius

    def bounds(self):
        # this can be tightened up, if need be. For now, just returns bounds for
        # a circle at (x,y), radius same as us, under the assumption that it's
        # better to have bounds() too big than too small.
        return (self.x - self.radius, self.y - self.radius,
                self.x + self.radius, self.y + self.radius)

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
        self.points = [Point(x,y)]
        self.radius = radius

    def bounds(self):
        x, y, r = self.x, self.y, self.radius
        return (x-r, y-r, x+r, y+r)

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
        self.points= [Point(x,y)]
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

    def bounds(self):
        # FIXME Absolutely no clue how to make this dependably correct
        p = self.points[0]
        return (p.x - 10, p.y - 10, p.x + 10, p.y + 10)

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
        self.points = [Point(p1), Point(p2)]


    def json(self):
        """ return a dict for json outputting """
        return {
                "type":self.type,
                "p1":self.points[0].json(),
                "p2":self.points[1].json(),
                }


class Polygon(Shape):
    """ A polygon is just a list of points, drawn as connected in order """
    #TODO should clear up if this is strictly a closed polygon, or if an open
    # polygon is valid as well. If strictly closed, does an n-gon need n points,
    # or n+1 points (does the start/end point need to be repeated)?

    def __init__(self, pts=[]):
        self.points = map(Point, pts)
        self.type = "polygon"


    def addPoint(self, pt):
        self.points.append(Point(pt))


    def json(self):
        return {
            "type":self.type,
            "points": [pt.json() for pt in self.points],
        }


class BezierCurve(Shape):
    """ A parametric curved line """

    def __init__(self,control1,control2,p1,p2):
        self.type = "bezier"
        self.points = map(Point, (p1, control1, control2, p2))

    def json(self):
        """ return a dict for json outputting """
        return {
                "type":self.type,
                "control1":self.points[1].json(),
                "control2":self.points[2].json(),
                "point1":self.points[0].json(),
                "point2":self.points[3].json(),
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

