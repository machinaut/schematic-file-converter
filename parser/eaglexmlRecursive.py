#!/usr/bin/env python
#
# Basic Strategy
# 1) Write Parser
# 2) Create Design
# 3) ...
# 4) Profit!

from core.design import *
from core.component import *
from core.instance import *
from core.shape import *
from xml.etree.ElementTree import ElementTree


class EagleXML:
	""" The Eagle XML Format Parser """
	def __init__(self):
	
	def parse(self, filename):
		""" Parse an Eagle XML file into a design """
		circuit = Design()
		#import an xmltree from the file provided
		xmltree = ElementTree(file=filename)
		root = xmltree.getroot()

