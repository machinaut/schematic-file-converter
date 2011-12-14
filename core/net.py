#!/usr/bin/env python
from shape import Point

class Net:
    """ a Net with metadata and a list of points (with connections)
    Internal representation of a net, closely matches JSON net """

    def __init__(self, net_id):
        self.net_id = net_id
        self.points = dict()
        self.attributes = dict()
        self.annotations = list()


    def bounds(self):
        """ Return the min and max points of the bounding box """
        xs = [p.x for p in self.points.values()]
        ys = [p.y for p in self.points.values()]
        bounds = [a.bounds() for a in self.annotations]
        xs += sum([list(b[0::2]) for b in bounds], [])
        ys += sum([list(b[1::2]) for b in bounds], [])
        return [Point(min(xs), min(ys)), Point(max(xs), max(ys))]


    def add_annotation(self, annotation):
        """ Add an annotation """
        self.annotations.append(annotation)


    def add_attribute(self, key, value):
        """ Add an attribute """
        self.attributes[key] = value


    def add_point(self, p):
        """ Add a point p to the net """
        self.points[p.point_id] = p

    def conn_point(self, a, b):
        """ connect point b to point a """
        self.points[a.point_id].connected_points.append(b.point_id)


    def connected(self, seg):
        """ is segment connected to this net """
        a, b = seg
        return a.point_id in self.points or b.point_id in self.points


    def connect(self, seg):
        """ connect segment to this net """
        a, b = seg
        if a.point_id not in self.points:
            self.add_point(a)
        self.conn_point(a, b)
        if b.point_id not in self.points:
            self.add_point(b)
        self.conn_point(b, a)

    def json(self):
        """ Return a net as JSON """
        return {
            "net_id":self.net_id,
            "attributes":self.attributes,
            "annotations":[a.json() for a in self.annotations],
            "points":[p.json() for p in self.points.values()]
            }


class NetPoint:
    """ A point, basic element in a net """

    def __init__(self, point_id, x, y):
        self.point_id = point_id
        self.x = x
        self.y = y
        self.connected_points = list()
        self.connected_components = list()


    def add_connected_point(self, point_id):
        """ Add a connected point """
        self.connected_points.append(point_id)


    def add_connected_component(self, connected_component):
        """ Add a connected component """
        self.connected_components.append(connected_component)


    def json(self):
        """ Return a netpoint as JSON """
        return {
            "point_id" : self.point_id,
            "x" : self.x,
            "y" : self.y,
            "connected_points" : self.connected_points,
            "connected_components" :
                [cc.json() for cc in self.connected_components]
            }


class ConnectedComponent:
    """ Object representing a component connected to a net """

    def __init__(self, instance_id, pin_number):
        self.instance_id = instance_id
        self.pin_number = pin_number


    def json(self):
        """ Return a connected component as JSON """
        return {
            "instance_id" : self.instance_id,
            "pin_number" : self.pin_number
            }
