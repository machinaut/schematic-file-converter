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

## Object types ##

A schematic/symbol file for gEDA/gaf consists of:

 * A version (v) as the first item in the file. This is required.
 * Any number of objects and the correct data. Objects are specified by an “object type”
 * Most objects are a single line, however text objects are two lines long.
 * No blank lines at the end of the file (these are ignored by the tools)
 * For all enumerated types in the gEDA/gaf file formats, the field takes on the numeric value.

The “object type” id is a single letter and this id must start in the
first column. The object type id is case sensitive. The schematic and
symbol files share the same file layout. A symbol is nothing more than
a collection of primitive objects (lines, boxes, circles, arcs, text,
and pins). A schematic is a collection of symbols (components), nets,
and buses.
The following sections describe the specifics of each recognized object
type. Each section has the name of the object, which file type (sch/sym)
the object can appear in, the format of the data, a description of each
individual field, details and caveats of the fields, and finally an
example with description.
For information on the color index (which is used in practically all
objects), see the Color section.

### version ###

Valid in: Schematic and Symbol files

**type version fileformat_version**

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>v</td>
	</tr>
	<tr>
		<td>1</td>
		<td>version</td>
		<td>int</td>
		<td>version of gEDA/gaf that wrote this file</td>
	</tr>
	<tr>
		<td>2</td>
		<td>fileformat_version</td>
		<td>int</td>
		<td>gEDA/gaf file format version number</td>
	</tr>
</table>

 * The type is a lower case “v” (as in Victor).
 * This object must be in every file used or created by the gEDA/gaf tools.
 * The format of the first version field is YYYYMMDD.
 * The version number is not an arbitrary timestamp. Do not make up a version number and expect the tools to behave properly.
 * The “version of gEDA/gaf that wrote this file” was used in all versions of gEDA/gaf up to 20030921 as the file formats version. This field should no longer be used to determine the file format. It is used for information purposes only now.
 * Starting at and after gEDA/gaf version 20031004, the fileformat version field is used to determine the file format version. All file format code should key off of this field.
 * fileformat version increases when the file format changes.
 * The starting point for fileformat version was 1. The current fileformat is 2.
 * fileformat version is just an integer with no minor number.
 * Development versions include: 19990601, 19990610, 19990705, 19990829, 19990919, 19991011, 20000220, 20000704, 20001006, 20001217, 20010304, 20010708, 20010722, 20020209, 20020414, 20020527, 20020825, 20021103, 20030223, 20030525, 20030901, 20040111, 20040710, 20041228, 20050313, 20050820, 20060123, 20060824, 20060906, 20061020, 20070216, 20070705, 20070708, 20070818, 20071229, 20080110, 20080127, 20080706, 20081220, 20081221, 20090328, 20090829, 20090830, 20110116, 20110619
 * Stable versions include: 20070526, 20070626, 20070902, 20071231, 20080127, 20080929, 20081220, 20081231, 20091004, 20100214, 20110115
 * CVS or test versions (should not be used): 20030921, 20031004, 20031019, 20031231, 20050814
 * Keep in mind that each of the above listed versions might have had file format variations. This document only covers the last version's file format.

Example:
<code>
	v 20040111 1
</code>




<table>
	<tr>
		<th></th>
		<th></th>
		<th></th>
		<th></th>
	</tr>
	<tr>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
	</tr>
</table>
