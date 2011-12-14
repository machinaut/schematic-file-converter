#!/usr/bin/env python
#
# Basic Strategy
# 0) 1:1 Input of the data model

import json
import core
from core.annotation import *
from core.component_instance import *
from core.components import *
from core.design import *
from core.design_attributes import *
from core.shape import *
from core.net import *

class JSON:
    """ The Open JSON Format Parser
    This is mostly for sanity checks, it reads in the Open JSON format,
    and then outputs it. """

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
            symbol_index = int(instance.get('symbol_index'))
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
        if visible is not None and visible.lower() == 'false':
            visible = 'false'
        else:
            visible = 'true'
        return Annotation(value,x,y,rotation,visible)


    def parse_components(self, components):
        for library_id,component in components.items():
            name = component.get('name')
            c = Component(name)
            # Get attributes
            for key,value in component.get('attributes').items():
                c.add_attribute(key,value)
            for symbol in component.get('symbols'):
                s = self.parse_symbol(symbol)
                c.add_symbol(s)
            self.design.add_component(library_id,c)


    def parse_symbol(self, symbol):
        s = Symbol()
        for body in symbol.get('bodies'):
            b = self.parse_body(body)
            s.add_body(b)
        return s


    def parse_body(self, body):
        b = Body()
        for pin in body.get('pins'):
            p = self.parse_pin(pin)
            b.add_pin(p)
        for shape in body.get('shapes'):
            s = self.parse_shape(shape)
            b.add_shape(s)
        return b


    def parse_pin(self,pin):
        pin_number = pin.get('pin_number')
        p1 = self.parse_point(pin.get('p1'))
        p2 = self.parse_point(pin.get('p2'))
        if None != pin.get('pin_label'):
            pin_label = self.parse_label(pin.get('pin_label'))
            return Pin(pin_number,p1,p2,pin_label)
        return Pin(pin_number,p1,p2)


    def parse_point(self,point):
        x = int(point.get('x'))
        y = int(point.get('y'))
        return Point(x,y)

    def parse_label(self,label):
        x = int(label.get('x'))
        y = int(label.get('y'))
        text = label.get('text')
        align = label.get('align')
        rotation = float(label.get('rotation'))
        return Label(x,y,text,align,rotation)

    def parse_shape(self,shape):
        typ = shape.get('type')
        if 'rectangle' == typ:
            x = int(shape.get('x'))
            y = int(shape.get('y'))
            height = int(shape.get('height'))
            width = int(shape.get('width'))
            return Rectangle(x,y,width,height)
        elif 'rounded_rectangle' == typ:
            x = int(shape.get('x'))
            y = int(shape.get('y'))
            height = int(shape.get('height'))
            width = int(shape.get('width'))
            radius = int(shape.get('radius'))
            return RoundedRectangle(x,y,width,height,radius)
        elif 'arc' == typ:
            x = int(shape.get('x'))
            y = int(shape.get('y'))
            start_angle = float(shape.get('start_angle'))
            end_angle = float(shape.get('end_angle'))
            radius = int(shape.get('radius'))
            return Arc(x,y,start_angle,end_angle,radius)
        elif 'circle' == typ:
            x = int(shape.get('x'))
            y = int(shape.get('y'))
            radius = int(shape.get('radius'))
            return Circle(x,y,radius)
        elif 'label' == typ:
            x = int(shape.get('x'))
            y = int(shape.get('y'))
            rotation = float(shape.get('rotation'))
            text = shape.get('text')
            align = shape.get('align')
            return Label(x,y,text,align,rotation)
        elif 'line' == typ:
            p1 = self.parse_point(shape.get('p1'))
            p2 = self.parse_point(shape.get('p2'))
            return Line(p1,p2)
        elif 'polygon' == typ:
            p = Polygon()
            for point in shape.get('points'):
                p.addPoint(self.parse_point(point))
            return p
        elif 'bezier' == typ:
            control1 = self.parse_point(shape.get('control1'))
            control2 = self.parse_point(shape.get('control2'))
            p1 = self.parse_point(shape.get('p1'))
            p2 = self.parse_point(shape.get('p2'))
            return BezierCurve(control1,control2,p1,p2)


    def parse_design_attributes(self, design_attributes):
        da = DesignAttributes()
        # Get the Annotations
        for annotation in design_attributes.get('annotations'):
            a = self.parse_annotation(annotation)
            da.add_annotation(a)

        # Get the Attributes
        for key,value in design_attributes.get('attributes').items():
            da.add_attribute(key, value)

        # Get the Metadata
        m = self.parse_metadata(design_attributes.get('metadata'))
        da.set_metadata(m)
        self.design.set_design_attributes(da)


    def parse_metadata(self, metadata):
        m = Metadata()
        m.set_name(metadata.get('name'))
        m.set_license(metadata.get('license'))
        m.set_owner(metadata.get('owner'))
        m.set_updated_timestamp(metadata.get('updated_timestamp'))
        m.set_design_id(metadata.get('design_id'))
        m.set_description(metadata.get('description'))
        m.set_slug(metadata.get('slug'))
        for attached_url in metadata.get('attached_urls'):
            m.add_attached_url(attached_url)
        return m


    def parse_nets(self, nets):
        for net in nets:
            net_id = net.get('net_id')
            n = Net(net_id)
            # Add Annotations
            for annotation in net.get('annotations'):
                a = self.parse_annotation(annotation)
                n.add_annotation(a)
            # Get the Attributes
            for key,value in net.get('attributes').items():
                n.add_attribute(key, value)
            # Get the Points
            for net_point in net.get('points'):
                np = self.parse_net_point(net_point)
                n.add_point(np)
            self.design.add_net(n)


    def parse_net_point(self,net_point):
        point_id = net_point.get('point_id')
        x = int(net_point.get('x'))
        y = int(net_point.get('y'))
        np = NetPoint(point_id,x,y)
        # Get the connected points
        for point in net_point.get('connected_points'):
            np.add_connected_point(point)
        # Get the ConnectedComponents
        for connectedcomponent in net_point.get('connected_components'):
            cc = self.parse_connected_component(connectedcomponent)
            np.add_connected_component(cc)
        return np


    def parse_connected_component(self,connectedcomponent):
        instance_id = connectedcomponent.get('instance_id')
        pin_number = connectedcomponent.get('pin_number')
        return ConnectedComponent(instance_id, pin_number)

if __name__ == '__main__':
  #Test case
  test = JSON()
  test.parse('/home/m/Downloads/High-Voltage-Converter-90V-From-15V.upv')
  open('./trololoTest.json', 'w').write(test.design.json())
