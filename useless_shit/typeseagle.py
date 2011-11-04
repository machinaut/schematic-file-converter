#!/usr/bin/env python
# OH GOD I MESSED UP THE EAGLE FILE FORMAT DEFINITION
# fix it
import json, copy
eagle = json.loads(open("eaglee.json").read())
a = copy.deepcopy(eagle)
basic = ["int","string","real"]

types = {}

for atype,members in a.items():
  for member,memtype in members.items():
    if memtype not in basic and member != memtype:
      if member not in types:
        types[member] = memtype
      elif types[member] != memtype:
        print "oh god why"

#f = open("types.json","w")
#f.write(json.dumps(types, sort_keys=True, indent=4))

