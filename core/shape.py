#!/usr/bin/env python

class Shape:
	"""a Shape with metadata and a list of shape parts
	Iternal representation of the shapes, closely matches JSON shapes """

	def __init__(self):
		self.kind = None

class Rectangle(Shape):

	def __init__(self,x,y,width,height):
		""" x and y are from the top left corner of the rectangle """
		self.kind = "rectangle"
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	@classmethod
	def fromCorners(cls,x,y,x2,y2):
		""" x and y are the top left corner of the rectangle, x2 and y2 are the
		bottom right corner of the rectangle """
		x = x
		y = y
		width = x2-x
		height = y2-y
		return cls(x,y,width,height)
	def json(self):
		""" return a dict for json outputting """
		return {
				"height":self.height,
				"type":self.kind,
				"width":self.width,
				"x":self.x,
				"y":self.y,
				}

class RoundedRectangle(Shape):

	def __init__(self,x,y,width,height,radius):
		""" x and y are from the top left corner of the rectangle """
		self.kind = "rounded_rectangle"
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
				"type":self.kind,
				"width":self.width,
				"x":self.x,
				"y":self.y,
				"radius":self.radius,
				}

class Arc(Shape):

	def __init__(self,x,y,start_angle,end_angle,radius):
		self.kind = "arc"
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
				"type":self.kind,
				"radius":self.radius,
				"x":self.x,
				"y":self.y,
				}

class Circle(Shape):

	def __init__(self,x,y,radius):
		self.kind = "circle"
		self.x = x
		self.y = y
		self.radius = radius
	def json(self):
		""" return a dict for json outputting """
		return {
				"radius":self.radius,
				"type":self.kind,
				"x":self.x,
				"y":self.y,
				}

class Label(Shape):

	def __init__(self,x,y,text,align,rotation):
		self.kind = "label" 
		self.x = x
		self.y = y
		self.text = text
		self.align = align
		self.rotation = rotation
	def json(self):
		""" return a dict for json outputting """
		return {
				"type":self.kind,
				"align":self.align,
				"rotation":self.rotation,
				"text":self.text,
				"x":self.x,
				"y":self.y,
				}

class Line(Shape):

	def __init__(self,x1,y1,x2,y2):
		self.kind = "line" 
		self.p1 = {"x":x1,"y":y1}
		self.p2 = {"x":x1,"y":y1}
	def json(self):
		""" return a dict for json outputting """
		return {
				"type":self.kind,
				"p1":self.p1,
				"p2":self.p2,
				}

class Polygon(Shape):

	def __init__(self):
		self.kind = "polygon" 
		self.points = dict({"points":list()})
	def addPoint(self, x, y):
		self.points["points"].append(dict({"x":x,"y":y}))
	def json(self):
		""" return a dict for json outputting """
		return {
				"type":self.kind,
				"points":self.points,
				}

class Biezer_Curve(Shape):

	def __init__(self,control1x,control1y,control2x,control2y,point1x,
				point1y,point2x,point2y):
		self.kind = "bezier" 
		self.control1 = dict({"x":control1x,"y":control1y})
		self.control2 = dict({"x":control2x,"y":control2y})
		self.point1 = dict({"x":point1x,"y":point1y})
		self.point2 = dict({"x":point2x,"y":point2y})
	def json(self):
		""" return a dict for json outputting """
		return {
				"type":self.kind,
				"control1":self.control1,
				"control2":self.control2,
				"point1":self.point1,
				"point2":self.point2,
				}
