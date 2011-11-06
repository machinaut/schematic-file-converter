class uvp:
	"""A class that handles uvp files."""

	def __init__(self):

class file_version:
"""
File Version

Used to identify the source of the export and the file version begin used.

file_version (string)
A string representing the file format version used.
exporter (string)
The source of the file.
"""

	def __init__(self):

class component_instances:
"""
Used to store all of the component instances (think reference designators, or symbols) in the schematic. Each instance will reference back to a component in the library (also exported in the components section). An instance has symbol position information, annotations, and attributes.

instance_id (string)
The unique id for this instance.
library_id (string)
The id that corresponds to the component (of which this is an instance) in the components section.
symbol_index (string)
The index of the symbol variant used for this instance.
symbol_attributes (array)
A collection of attributes about each symbol instance in the schematic. The array index corresponds to the body index of the symbol variant. Normally this is an array of size one, but this allows for multi-body symbols.
x (integer)
The top left corner of the symbol, X-coordinate.
y (integer)
The top left corner of the symbol, Y-coordinate.
rotation (integer)
In pi radians, step size of 0.5 (nominally zero).
annotations (annotations)
The associated annotations.
attributes (attributes)
The instance attributes.
"""
	def __init__(self):

class nets:

	def __init__(self):

class design_attributes:

	def __init__(self):

class components:

	def __init__(self):
