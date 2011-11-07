#!/usr/bin/env python
#
# Basic Strategy
# 0) 1:1 Input of the data model

import json
from core.annotation import *
from core.design import *
from core.component_instance import *

class JSON:
    """ The JSON Format Parser """

    def __init__(self):
        self.design = Design()


    def parse(self, filename):
        f = open(filename)
        read = json.loads(f.read())
        f.close()

        self.parse_component_instances(read.get('component_instances'))
        self.parse_components(read.get('components'))
        self.parse_design_attributes(read.get('design_attributes'))
        self.parse_nets(read.get('nets'))
        self.parse_version(read.get('version'))
        return self.design


    def parse_version(self, version):
        file_version = version.get('file_version')
        exporter = version.get('exporter')
        self.design.set_version(file_version,exporter)


    def parse_component_instances(self, component_instances):
        for instance in component_instances:
            # Get instance_id, library_id and symbol_index
            instance_id = instance.get('instance_id')
            library_id = instance.get('library_id')
            symbol_index = instance.get('symbol_index')
            # Make the ComponentInstance()
            inst = ComponentInstance(instance_id, library_id, symbol_index)

            # Get the SymbolAttributes
            for symbol_attribute in instance.get('symbol_attributes'):
                sa = self.parse_symbol_attribute(symbol_attribute)
                inst.add_symbol_attribute(sa)

            # Get the Attributes
            for key,value in instance.get('attributes').items():
                inst.add_attribute(key, value)

            # Add the ComponentInstance
            self.design.add_component_instance(inst)


    def parse_symbol_attribute(self, symbol_attribute):
        x = int(symbol_attribute.get('x'))
        y = int(symbol_attribute.get('y'))
        rotation = float(symbol_attribute.get('rotation'))
        # Make SymbolAttribute
        sa = SymbolAttribute(x,y,rotation)
        # Add Annotations
        for annotation in symbol_attribute.get('annotations'):
            a = self.parse_annotation(annotation)
            sa.add_annotation(a)
        # Return SymbolAttribute to be added to it's ComponentInstance
        return sa


    def parse_annotation(self, annotation):
        value = annotation.get('value')
        x = int(annotation.get('x'))
        y = int(annotation.get('y'))
        rotation = float(annotation.get('rotation'))
        visible = annotation.get('visible')
        if visible.lower() == 'false':
            visible = 'false'
        else:
            visible = 'true'
        return Annotation(value,x,y,rotation,visible)


    def parse_components(self, components):
        pass
    def parse_design_attributes(self, design_attributes):
        pass
    def parse_nets(self, nets):
        pass
