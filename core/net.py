#!/usr/bin/env python

class Net:
    """ a Net with metadata and a list of points (with connections)
    Internal representation of a net, closely matches JSON net """

    def __init__(self):
        self.net_id = ""
        self.points = {} # dict to make looking up points easier, outputted as array
        self.attributes = []
        self.annotations = []


    def add_annotation(self, annotation):
        self.annotations.append(annotation)


    def addpoint(self,p):
        """ Add a point p to the net """
        self.points[p] = {
            "point_id": p, # use the point tuples as ID's
            "x":p[0],
            "y":p[1],
            "connected_components": [],
            "connected_points": set()
            }


    def connpoint(self,a,b):
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


    def prettypoints(self):
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
        """ return a dict for json outputting """
        return {
            "attributes":self.attributes,
            "annotations":[a.json() for a in self.annotations],
            "net_id":self.net_id,
            "points":self.prettypoints()
            }


