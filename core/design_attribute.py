#!/usr/bin/env python

from time import time

class Design_Attribute:
	"""This is a class that defines a Design_Attribute, and provides useful
	methods for working with the Design_attribute portion of the upv json
	file. """
	def __init__(self):
		self.annotations = []
		self.attributes = dict()
		self.metadata = {
				"name":"", # TODO: make this name reflect the name from eagle
				"license":"", # TODO: add license selection to upconvert.py
				"owner":"",
				"updated_timestamp": int(time()),
				"design_id": "",
				"description":"",
				"slug":,
				"attached_urls":[],
				}

	def add_attribute(self, attribute):
		self.attributes[attribute.key] = attribute.value

	def json(self):
		return {"design_attributes" : {
				"annotations" : self.annotations,
				"metadata" : self.metadata,
				"attributes" : self.attributes,
				}
