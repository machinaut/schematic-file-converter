#!/usr/bin/env python

class Shape:
	"""a Shape with metadata and a list of shape parts
	Iternal representation of the shapes, closely matches JSON shapes """

	def __init__(self):
		self.kind = None

class Rectangle(Shape):

	def __init__(self,x,y,width,height):
		self.kind = "rectangle"
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	@classmethod
	def fromCorners(cls,x,y,x2,y2):
		x = x
		y = y
		width = x2-x
		height = y2-y
		return cls(x,y,width,height)

class RoundedRectangle(Shape):

	def __init__(self,x,y,width,height,radius):
		self.kind = "roundedrectangle"
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.radius = radius
	@classmethod
	def fromCorners(cls,x,y,x2,y2,radius):
		x = x
		y = y
		width = x2-x
		height = y2-y
		radius = radius
		return cls(x,y,width,height,radius)

class Arc(Shape):

	def __init__(self,x,y,start_angle,end_angle,radius):
		self.kind = "arc"
		self.x = x
		self.y = y
		self.start_angle = start_angle
		self.end_angle = end_angle
		self.width = width
		self.height = height
		self.radius = radius

class Circle(Shape):

	def __init__(self,x,y,radius):
		self.kind = "circle"
		self.x = x
		self.y = y
		self.radius = radius

class Label(Shape):

	def __init__(self,x,y,text,align,rotation):
		self.kind = "label" 
		self.x = x
		self.y = y
		self.text = text
		self.align = align
		self.rotation = rotation

class Line(Shape):

	def __init__(self,x1,y1,x2,y2):
		self.kind = "line" 
		self.p1 = (x1,y1)
		self.p2 = (x2,y2)

class Polygon(Shape):

	def __init__(self):
		self.kind = "polygon" 
		self.points = dict({"points":list()})

class Biezer_Curve(Shape):

	def __init__(self,control1,control2,point1,point2):
		self.kind = "bezier" 
		self.control1 = control1
		self.control2 = control2
		self.point1 = point1
		self.point2 = point2


