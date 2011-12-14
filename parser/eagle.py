#!/usr/bin/env python
#
# Basic Strategy
# 0) ...
# 1) ???
# 2) Profit!!!
from core.design import Design
from xml.etree.ElementTree import ElementTree


class Eagle:
    """ The Eagle Format Parser """

    def __init__(self):
        pass


    def parse(self, filename):
        """ Parse an Eagle file into a design """
<<<<<<< HEAD
        #design = design()
        #import an xmltree from the file provided
       	xmltree = ElementTree(file=filename)
        xmlroot = xmltree.getroot()
		
        return xmltree
=======
        design = Design()
        f = open(filename, "w")
        #TODO: Read!
        f.close()
        return design
>>>>>>> 5abb89ac932f010195dea31c734cf01a4d7fff5f
