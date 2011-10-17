#!/usr/bin/env python
# render.py - quick and dirty script to try rendering JSON format

import json, sys
from PIL import Image, ImageDraw

ckt = json.loads(open("example.json").read())
print "processing", ckt["sheet"]["attributes"]["name"]

im = Image.new("RGB",(400,400))
draw = ImageDraw.Draw(im)

draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)

im.save(sys.stdout, "PNG")
