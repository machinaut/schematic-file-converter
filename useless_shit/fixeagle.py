#!/usr/bin/env python
# OH GOD I MESSED UP THE EAGLE FILE FORMAT DEFINITION
# fix it
import json, copy
eagle = json.loads(open("eagle511.json").read())
a = copy.deepcopy(eagle)
b = copy.deepcopy(eagle)

for atype,members in a.items():
  for member,memtype in members.items():
    if type(memtype) == type([]):
      eagle[atype][member] = memtype[1]
    if memtype == "object":
      eagle[atype][member] = member

f = open("eaglee.json","w")
f.write(json.dumps(eagle, sort_keys=True, indent=4))

