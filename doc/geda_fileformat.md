# gEDA/gaf File Format Document #

by: Ales V. Hvezda, ahvezda@geda.seul.org
This document is released under [GFDL](http://www.gnu.org/copyleft/fdl.html)
December 31st, 2003

## Overview ##

This file is the official documentation for the file formats in gEDA/gaf
(gschem And Friends). The primary file format used in gEDA/gaf is the
schematic/symbol format. Files which end with .sch or .sym are schematics
or symbol files. Until there is another file type in gEDA/gaf, then this
document will only cover the symbol/schematic file format.
This file format document is current as of gEDA/gaf version 20040111.
This document covers file format version 1 and 2.
Note, this file format and any other file formats associated with gEDA
are placed under the General Public License (GPL) version 2.0. The
gEDA/gaf symbol and schematic file format is Copyright (C) 1998-2004
Ales Hvezda.

## Coordinate Space ##

All coordinates are in mils (1/1000 of an inch). This is an arbitrary decision. Remember in there is no concept of physical lengths/dimensions in schematics and symbols (for schematic capture only).

 * Origin is in lower left hand corner.
 * The size of the coordinate space is unlimited, but it is recommended that all objects stay within (120.0, 90.0) (x, y inches).
 * It is generally advisable to have positive x and y coordinates, however, negative coordinates work too, but not recommended.

The following figure shows how the coordinate space is setup: 
TODO: insert image

X axis increases going to the right. Y axis increase going up. Coordinate system is landscape and corresponds to a sheet of paper turned on its side.

## Filenames ##

Symbols end in .sym. The only symbol filename convention that is used in gEDA/gaf is that if there are multiple instances of a symbol with the same name (like a 7400), then a -1, -2, -3, … -N suffix is added to the end of the filename. Example: 7400-1.sym, 7400-2.sym, 7400-3.sym…
Schematics end in .sch. There used to be a schematic filename convention (adding a -1 .. -N to the end of the basename), but this convention is now obsolete. Schematic filenames can be anything that makes sense to the creator.
