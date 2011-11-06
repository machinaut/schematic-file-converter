#!/usr/bin/env python

class Shape:
	"""A shape with metadata and a list of shape parts
	Internal representation of a shape, closely matches JSON shape """

	def __init__(self):
		self.x
		self.y

class Rectangle(Shape):

	def __init__(self):
		self.width
		self.height

class Rounded_Rectangle(Shape):

	def __init__(self):
		self.width
		self.height
		self.radius

class Arc(Shape):
	start angle
	end angle
	radius

	def __init__(self):
		self.start_angle
		self.end_angle
		self.radius

class Circle(Shape):
	def __init__(self):
		self.radius

class Label(Shape):
	def __init__(self):
		self.text
		self.align
		self.rotation

class Line(Shape):
	def __init__(self):
		self.p1
		self.p2

class Polygon(Shape):
	def __init__(self):

class Biezer_Curve(Shape):
	def __init__(self):


