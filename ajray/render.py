#!/usr/bin/env python
# render.py - quick and dirty script to try rendering JSON format
# TODO: this does no error checking of the input file, that'd be nice mkay?
# TODO: class-ify this, instead of handing the 'draw' instance around

import json, sys
from PIL import Image, ImageDraw

def drawCircuit(circuit, draw):
  """ draw a circuit to a draw instance """
  sheet = circuit["sheet"]
  drawSheet(sheet, draw)
  components = circuit["components"]
  instances = circuit["instances"]
  drawComponents(components,instances,draw)

def drawSheet(sheet, draw):
  """ draw the 'sheet' part of a circuit """
  # Draw annotations (notes)
  for name,note in sheet["annotations"].items():
    value = sheet["attributes"][name]
    position = ( int(note["x"]), int(note["y"]) )
    drawNote(position, value, draw)
  # Draw shapes
  for name,shape in sheet["shapes"].items():
    drawShape((0,0),shape,draw) # Everything in sheet relative to origin

def drawNote(pt, text, draw):
  """ draw an annotation at a point """
  #TODO align other than top left, rotation other than normal
  draw.text(pt, text, fill=(255,255,0))

def drawShape(pt, shape,draw):
  """ draw from a set of shapes relative to a point """
  if   shape["type"] == "line":
    pos = [int(i) for i in (shape["x1"],shape["y1"],shape["x2"],shape["y2"])]
    pos = (pos[0]+ pt[0],pos[1]+pt[1], pos[2]+pt[0],pos[3]+pt[1])
    draw.line(pos)
  elif shape["type"] == "rect":
    pos = [int(i) for i in (shape["x1"],shape["y1"],shape["x2"],shape["y2"])]
    pos = (pos[0]+ pt[0],pos[1]+pt[1], pos[2]+pt[0],pos[3]+pt[1])
    draw.rectangle(pos)

def drawComponents(comps, inst, draw):
  """ draw instances of components """
  # TODO: yeah my variable names sometimes suck
  for name,comp in inst.items(): # iterate over instances
    symb = comp["symbol"]
    for na,body in comp["bodies"].items(): # iterate over bodies
      #TODO: support annotations, rotation and other fun stuff
      pos = [int(i) for i in (body["x"],body["y"])]
      drawBody(pos, comps[name], symb, na, draw)

def drawBody(pt, comp, symb, body, draw):
  """ draw a body of a component """
  body = comp["symbols"][symb]["bodies"][body]
  # Draw annotations (notes)
  for name,note in body["annotations"].items():
    value = body["attributes"][name]
    pos = ( int(note["x"]), int(note["y"]) )
    pos = (pos[0]+ pt[0],pos[1]+pt[1])
    drawNote(pos, value, draw)
  # Draw shapes
  for name,shape in body["shapes"].items():
    drawShape(pt,shape,draw) # Everything in sheet relative to origin


if __name__ == "__main__":
  ckt = json.loads(open("example.json").read())

  # Draw circuit to an image, then save it out
  im = Image.new("RGB",(100,100))
  draw = ImageDraw.Draw(im)
  drawCircuit(ckt,draw)
  im.save("example.png", "PNG")
