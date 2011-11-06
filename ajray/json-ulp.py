#!/usr/bin/env python
# json-ulp.py - generate json.ulp, which exports Eagle to JSON
# http://github.com/ajray/schematic-file-converter
# Alex Ray (2011) <ajray@ncsu.edu>
# TODO handle loop members
import copy
from eaglet import eagle, types, basic, header, misc
def typ(a):
  """ 
  Given a member name, return it's type
  Basically 'types' is a reverse-lookup for all the members
  in 'eagle.json' that is made at runtime by 'import eaglet'
  """
  if a in basic: return a
  if a in types: return types[a]
  return "UL_"+a.upper()


def printfuncheader(name):
  """ return the header to a printfunc with the given name """
  s = """
  void print_%s(%s %s_arg) {
    int a;
    print__opening("%s");
  """ % (name, typ(name), name, name)
  return s

def printfunccloser():
  """ return the closer to a printfunc """
  s = """
    print__closing();
  }
  """
  return s

def printfunc(name,members): 
  """ 
  Make a print_<type>() function for a type given it's members
  and their types

  This is code that generates code. Nasty shit 
  Basically it puts a head and a tail on it, and iterates over
  every "member" of the type, printing it.
  The end result is print functions for every type that call 
  print functions for every type within it.
  ...Like a recursive descent barfer.
  """
  print printfuncheader(name) # print the header

  com = False           # Keeping track of commas
  for mem,mtyp in members.items(): # Member fields of each type
    if not com: com = True # Taking care of commas
    else: print 'printf(",\n");'
    if mtyp not in basic and mem != mtyp: # loop member
      loop = mem+'_loop'
      print '\tpl(%s);a=0;%s.%s(%s){'%(mem,arg,mem,loop)
      print '\t\tif(a==0)a=1;else cn();%s("%s",%s);}'%(fun,mem,loop),
    else: # Normal data member
      print '\t%s("%s",%s.%s);'%(fun,mem,mem,mem), # data member
  print printfunccloser()

if __name__ == "__main__":
  print header
  print misc
  # print functions by dependencies
  found = True
  dependencies = {"string","int","real"}
  while found:
    found = False
    for name,member in eagle.items():
      good = True
      for mem,mtyp in member.items():
        if mtyp not in dependencies:
          good = False
      if good: # all dependencies met
        found = True
        dependencies.add(name)
        del eagle[name]
        print name
  print "=====notfound====="
  for name in eagle.iterkeys(): print name
  #for name,members in eagle.items(): printfunc(name,members)
