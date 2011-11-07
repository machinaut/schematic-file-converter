#!/usr/bin/env python

class Net:
    """ a Net with metadata and a list of points (with connections)
    Internal representation of a net, closely matches JSON net """

    def __init__(self,net_id):
        self.net_id = net_id
        self.points = list()
        self.attributes = dict()
        self.annotations = list()


    def add_annotation(self, annotation):
        self.annotations.append(annotation)
        

    def add_attribute(self, key, value):
        self.attribute[key] = value


    def add_point(self,p):
        """ Add a point p to the net """
        self.points[p] = {
            "point_id": p, # use the point tuples as ID's
            "x":p[0],
            "y":p[1],
            "connected_components": [],
            "connected_points": set()
            }


    def add_net_point(self,net_point):
        self.points.append(net_point)


    def conn_point(self,a,b):
        """ connect point b to point a """
        self.points[a]["connected_points"].add(b)


    def connected(self,seg):
        """ is segment connected to this net """
        a,b = seg
        return a in self.points or b in self.points


    def connect(self,seg):
        """ connect segment to this net """
        a,b = seg
        if a not in self.points:
            self.addpoint(a)
        self.connpoint(a,b)
        if b not in self.points:
            self.addpoint(b)
        self.connpoint(b,a)


    def pretty_points(self):
        """ return points array with point_id's instead of tuples """
        a = self.points.values()
        for p in a:
            p["connected_points"] = [self.point_id(i) for i in p["connected_points"]]
            p["point_id"] = self.point_id(p["point_id"])
        return a


    def point_id(self, p):
        """ point_id gives a point id of the form 6100x4950, which is unique for each point """
        return str(p[0])+"x"+str(p[1])


    def json(self):
        return {
            "net_id":self.net_id,
            "attributes":self.attributes,
            "annotations":[a.json() for a in self.annotations],
            "points":[p.json() for p in self.points]
            }


class NetPoint:
    """ A point, basic element in a net """

    def __init__(self,point_id,x,y):
        self.point_id = point_id
        self.x = x
        self.y = y
        self.connected_points = list()
        self.connected_components = list()

    def add_connected_point(self,point_id):
        self.connected_points.append(point_id)

    def add_connected_component(self,connected_component):
        self.connected_components.append(connected_component)

    def json(self):
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
        return {
            "instance_id" : self.instance_id,
            "pin_number" : self.pin_number
            }








