#!/usr/bin/env python
#
# Basic Strategy
# 1) Write Parser
# 2) Create Design
# 3) ...
# 4) Profit!

from core.design import Design
from xml.etree.ElementTree import ElementTree


class EagleXML:
    """ The Eagle XML Format Parser """

    def __init__(self):
        pass


    def parse(self, filename):
		design = design()

        """ Parse an Eagle XML file into a design """
        #import an xmltree from the file provided
       	xmltree = ElementTree(file=filename)
        xmlroot = xmltree.getroot()
		
        return xmltree
