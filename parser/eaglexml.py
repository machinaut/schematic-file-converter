#!/usr/bin/env python
#
# Basic Strategy
# 0) ...

from core.design import Design
from xml.etree.ElementTree import ElementTree


class EagleXML:
    """ The Eagle XML Format Parser """

    def __init__(self):
        pass


    def parse(self, filename):
        """ Parse an Eagle XML file into a design """
        #import an xmltree from the file provided
       	xmltree = ElementTree(file=filename)
        xmlroot = xmltree.getroot()
		
        return xmltree
