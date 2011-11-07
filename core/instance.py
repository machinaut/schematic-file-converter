#!/usr/bin/env python
import random
import shape

class Instance:
  def __init__(self, instance_id, library_id):
    self.instance_id = instance_id
    self.library_id = library_id
    self.symbol_index = list()
  
  def get_instance_id(self):
    return self.instance_id

