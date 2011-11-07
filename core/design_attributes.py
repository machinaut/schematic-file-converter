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


    def add_attribute(self, attribute):
        self.attributes[attribute.key] = attribute.value


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
        self.slug = ""
        self.attached_urls = list()


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


