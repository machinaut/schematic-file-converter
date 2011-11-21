#!/usr/bin/env python
#
# Basic Strategy
# 0) 1:1 Output of the data model

import json

class JSON:
    """ The JSON Format Writer """

    def __init__(self):
        pass

    def write(self, design, filename):
        """ Recursively ask for JSON forms of components for output """
        f = open(filename, "w")
        f.write(json.dumps(design.json(),sort_keys=True,indent=4))
        f.close()
        return
