#!/usr/bin/env python
import time

class DesignAttributes:
    """ The DesignAttributes class corresponds to the design_attributes
    object in the Open JSON format """

    def __init__(self):
        self.annotations = []
        self.attributes = dict()
        self.metadata = Metadata()

    def add_annotation(self, annotation):
        self.annotations.append(annotation)


    def add_attribute(self, key, value):
        self.attributes[key] = value


    def set_metadata(self, metadata):
        self.metadata = metadata

    def json(self):
        return {
            "annotations" : [a.json() for a in self.annotations],
            "metadata" : self.metadata.json(),
            "attributes" : self.attributes,
            }


class Metadata:
    """ The metadata of a DesignAttributes object """

    def __init__(self):
        self.name = "" # TODO: make this name reflect the name from eagle
        self.license = "" # TODO: add license selection to upconvert.py
        self.owner = ""
        self.updated_timestamp = int(time.time())
        self.design_id = ""
        self.description = ""
        self.slug = self.name.replace(' ','-')
        self.attached_urls = list()


    def set_name(self,name):
        self.name = name


    def set_license(self,license):
        self.license = license


    def set_owner(self,owner):
        self.owner = owner


    def set_updated_timestamp(self,updated_timestamp):
        self.updated_timestamp = int(updated_timestamp)


    def set_design_id(self,design_id):
        self.design_id = design_id


    def set_description(self,description):
        self.description = description


    def set_slug(self,slug):
        self.slug = slug


    def add_attached_url(self,attached_url):
        self.attached_urls.append(attached_url)


    def json(self):
        return {
            "name":self.name,
            "license":self.license,
            "owner":self.owner,
            "updated_timestamp": self.updated_timestamp,
            "design_id": self.design_id,
            "description": self.description,
            "slug": self.slug,
            "attached_urls":[]
            }


