#!/usr/bin/env python

from time import time

class Attribute:

	def __init__(self,name,license,owner):
		self.annotations = []
		self.attributes = dict()
		self.metadata = {
				"name":name,
				"license":license,
				"owner":owner,
				"updated_timestamp": int(time()),
				"design_id": 
				}

	def add_attribute

	def json(self):
		return
