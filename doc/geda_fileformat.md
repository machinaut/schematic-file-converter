# gEDA/gaf File Format Document #

by: Ales V. Hvezda, ahvezda@geda.seul.org
This document is released under [GFDL](http://www.gnu.org/copyleft/fdl.html)
December 31st, 2003

slight changes for readability by tpltnt, November 2011

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

Format: <pre>type version fileformat_version</pre>

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
<pre>v 20040111 1</pre>

### line ###

Valid in: Schematic and Symbol files

Format: <pre>type x1 y1 x2 y2 color width capstyle dashstyle dashlength dashspace</pre>

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
		<td>L</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x1</td>
		<td>int/mils</td>
		<td>First X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y1</td>
		<td>int/mils</td>
		<td>First Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>x2</td>
		<td>int/mils</td>
		<td>Second X coordinate</td>
	</tr>
	<tr>
		<td>4</td>
		<td>y2</td>
		<td>int/mils</td>
		<td>Second Y coordinate</td>
	</tr>
	<tr>
		<td>5</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>6</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of line</td>
	</tr>
	<tr>
		<td>7</td>
		<td>capstyle</td>
		<td>int</td>
		<td>Line cap style</td>
	</tr>
	<tr>
		<td>8</td>
		<td>dashstyle</td>
		<td>int</td>
		<td>Type of dash style</td>
	</tr>
	<tr>
		<td>9</td>
		<td>dashlength</td>
		<td>int/mils</td>
		<td>Length of dash</td>
	</tr>
	<tr>
		<td>10</td>
		<td>dashspace</td>
		<td>int/mils</td>
		<td>Space inbetween dashes</td>
	</tr>
</table>

 * The capstyle is an enumerated type:
  * END NONE = 0
  * END SQUARE = 1
  * END ROUND = 2
 * The dashstyle is an enumerated type:
  * TYPE SOLID = 0
  * TYPE DOTTED = 1
  * TYPE DASHED = 2
  * TYPE CENTER = 3
  * TYPE PHANTOM = 4
 * The dashlength parameter is not used for TYPE SOLID and TYPE DOTTED. This parameter should take on a value of -1 in these cases.
 * The dashspace parameter is not used for TYPE SOLID. This parameter should take on a value of -1 in these case.

Example: <pre>L 23000 69000 28000 69000 3 40 0 1 -1 75</pre>

A line segment from (23000, 69000) to (28000, 69000) with color index 3, 40 mils thick, no cap, dotted line style, and with a spacing of 75 mils in between each dot.


### picture ###

Valid in: Schematic and Symbol files

Format:<pre>type x1 y1 width height angle mirrored embedded
filename
[encoded picture data
encoded picture end]
</pre>

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
		<td>G</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>Lower left X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>Lower left Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of the picture</td>
	</tr>
	<tr>
		<td>4</td>
		<td>height</td>
		<td>int/mils</td>
		<td>Height of the picture</td>
	</tr>
	<tr>
		<td>5</td>
		<td>angle</td>
		<td>int/degrees</td>
		<td>Angle of the picture</td>
	</tr>
	<tr>
		<td>6</td>
		<td>mirrored</td>
		<td>char</td>
		<td>Mirrored or normal picture</td>
	</tr>
	<tr>
		<td>7</td>
		<td>embedded</td>
		<td>char</td>
		<td>Embedded or link to the picture file</td>
	</tr>
	<tr>
		<td>8</td>
		<td>filename</td>
		<td>string</td>
		<td>path and filename of a not embedded picture</td>
	</tr>
	<tr>
		<td>9</td>
		<td>encoded picture data</td>
		<td>string</td>
		<td>Serialized picture encoded using base64</td>
	</tr>
	<tr>
		<td>10</td>
		<td>encoded picture end</td>
		<td>string</td>
		<td>A line containing only a dot character</td>
	</tr>
	</tr>
</table>

 * This object is a picture object. The first line contains all the picture parameters, and the second line is the path and filename of the picture. The filename is not used if the picture is embedded.
 * The angle of the picture can only take on one of the following values: 0, 90, 180, 270.
 * The mirrored field is an enumerated type:
  * NOT MIRRORED = 0
  * MIRRORED = 1
 * The embedded field is an enumerated type:
  * NOT EMBEDDED = 0
  * EMBEDDED = 1 (not yet supported)
 * The encoded picture and encoded picture end fields are only in the file if the picture is embedded in the schematic:
  * encoded picture data: This is a multiple line field. The picture is serialized and then encoded using base64. This way the encoded data uses only printable characters. This field is the result of these two operations.
  * encoded picture end : A line containing only a single dot '.' character marks the end of the encoded picture data.

Example:
<pre>
G 16900 35800 1400 2175 0 0 0
../bitmaps/logo.jpg
</pre>

A picture object with the lower left corner at (16900, 35800). The width of the image is 1400 mils, and its height is 2175 mils. The picture rotation is 0 degrees and the picture is not mirrored, neither embedded.
The picture path and filename is showed in the second line.

Example:
<pre>
G 16900 35800 1400 2175 0 0 1
../bitmaps/logo.jpg
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
.
</pre>

A picture object with the lower left corner at (16900, 35800). The width of the image is 1400 mils, and its height is 2175 mils.
The picture rotation is 0 degrees, it is not mirrored, and it is embedded.
The picture path and filename is showed in the second line. Since this is an embedded picture, the filename and path are not used.
The encoded picture data is only an example (it is not real data). The last line containing a single dot '.' character marks the end of the encoded picture data. 

### box ###

Valid in: Schematic and Symbol files

Format: <pre>type x y width height color width capstyle dashstyle dashlength dashspace filltype fillwidth angle1 pitch1 angle2 pitch2</pre>

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
		<td>B</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>Lower left hand X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>Lower left hand Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of the box (x direction)</td>
	</tr>
	<tr>
		<td>4</td>
		<td>height</td>
		<td>int/mils</td>
		<td>Height of the box (y direction)</td>
	</tr>
	<tr>
		<td>5</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>6</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of lines</td>
	</tr>
	<tr>
		<td>7</td>
		<td>capstyle</td>
		<td>int/mils</td>
		<td>Line cap style</td>
	</tr>
	<tr>
		<td>8</td>
		<td>dashstyle</td>
		<td>int</td>
		<td>Type of dash style</td>
	</tr>
	<tr>
		<td>9</td>
		<td>dashlength</td>
		<td>int/mils</td>
		<td>Length of dash</td>
	</tr>
	<tr>
		<td>10</td>
		<td>dashspace</td>
		<td>int/mils</td>
		<td>Space inbetween dashes</td>
	</tr>
	<tr>
		<td>11</td>
		<td>filltype</td>
		<td>int</td>
		<td>Type of fill</td>
	</tr>
	<tr>
		<td>12</td>
		<td>fillwidth</td>
		<td>int/mils</td>
		<td>Width of the fill lines</td>
	</tr>
	<tr>
		<td>13</td>
		<td>angle1</td>
		<td>int/degrees</td>
		<td>First angle of fill</td>
	</tr>
	<tr>
		<td>14</td>
		<td>pitch1</td>
		<td>int/mils</td>
		<td>First pitch/spacing of fill</td>
	</tr>
	<tr>
		<td>15</td>
		<td>angle2</td>
		<td>int/degrees</td>
		<td>Second angle of fill</td>
	</tr>
	<tr>
		<td>16</td>
		<td>pitch2</td>
		<td>int/mils</td>
		<td>Second pitch/spacing of fill</td>
	</tr>
</table>

 * The capstyle is an enumerated type:
  * END NONE = 0
  * END SQUARE = 1
  * END ROUND = 2
 * The dashstyle is an enumerated type:
  * TYPE SOLID = 0
  * TYPE DOTTED = 1
  * TYPE DASHED = 2
  * TYPE CENTER = 3
  * TYPE PHANTOM = 4
 * The dashlength parameter is not used for TYPE SOLID and TYPE DOTTED. This parameter should take on a value of -1 in these cases.
 * The dashspace parameter is not used for TYPE SOLID. This parameter should take on a value of -1 in these case.
 * The filltype parameter is an enumerated type:
  * FILLING HOLLOW = 0
  * FILLING FILL = 1
  * FILLING MESH = 2
  * FILLING HATCH = 3
  * FILLING VOID = 4 unused
 * If the filltype is 0 (FILLING HOLLOW), then all the fill parameters should take on a value of -1.
 * The fill type FILLING FILL is a solid color fill.
 * The two pairs of pitch and spacing control the fill or hatch if the fill type is FILLING MESH.
 * Only the first pair of pitch and spacing are used if the fill type is FILLING HATCH.

Example:
<pre>B 33000 67300 2000 2000 3 60 0 2 75 50 0 -1 -1 -1 -1 -1</pre>

A box with the lower left hand corner at (33000, 67300) and a width and
height of (2000, 2000), color index 3, line width of 60 mils, no cap,
dashed line type, dash length of 75 mils, dash spacing of 50 mils, no
fill, rest parameters unset. 

### circle ###

Valid in: Schematic and Symbol files

Format: <pre>type x y radius color width capstyle dashstyle dashlength dashspace filltype fillwidth angle1 pitch1 angle2 pitch2</pre>

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
		<td>V</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>Center X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>Center Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>radius</td>
		<td>int/mils</td>
		<td>Radius of the circle</td>
	</tr>
	<tr>
		<td>4</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>5</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of circle line</td>
	</tr>
	<tr>
		<td>6</td>
		<td>capstyle</td>
		<td>int/mils</td>
		<td>0 unused</td>
	</tr>
	<tr>
		<td>7</td>
		<td>dashstyle</td>
		<td>int</td>
		<td>Type of dash style</td>
	</tr>
	<tr>
		<td>8</td>
		<td>dashlength</td>
		<td>int/mils</td>
		<td>Length of dash</td>
	</tr>
	<tr>
		<td>9</td>
		<td>dashspace</td>
		<td>int/mils</td>
		<td>Space inbetween dashes</td>
	</tr>
	<tr>
		<td>10</td>
		<td>filltype</td>
		<td>int</td>
		<td>Type of fill</td>
	</tr>
	<tr>
		<td>11</td>
		<td>fillwidth</td>
		<td>int/mils</td>
		<td>Width of the fill lines</td>
	</tr>
	<tr>
		<td>12</td>
		<td>angle1</td>
		<td>int/degrees</td>
		<td>First angle of fill</td>
	</tr>
	<tr>
		<td>13</td>
		<td>pitch1</td>
		<td>int/mils</td>
		<td>First pitch/spacing of fill</td>
	</tr>
	<tr>
		<td>14</td>
		<td>angle2</td>
		<td>int/degrees</td>
		<td>Second angle of fill</td>
	</tr>
	<tr>
		<td>15</td>
		<td>pitch2</td>
		<td>int/mils</td>
		<td>Second pitch/spacing of fill</td>
	</tr>
</table>

 * The dashstyle is an enumerated type:
  * TYPE SOLID = 0
  * TYPE DOTTED = 1
  * TYPE DASHED = 2
  * TYPE CENTER = 3
  * TYPE PHANTOM = 4
 * The dashlength parameter is not used for TYPE SOLID and TYPE DOTTED. This parameter should take on a value of -1 in these cases.
 * The dashspace parameter is not used for TYPE SOLID. This parameter should take on a value of -1 in these case.
 * The filltype parameter is an enumerated type:
  * FILLING HOLLOW = 0
  * FILLING FILL = 1
  * FILLING MESH = 2
  * FILLING HATCH = 3
  * FILLING VOID = 4 unused
 * If the filltype is 0 (FILLING HOLLOW), then all the fill parameters should take on a value of -1.
 * The fill type FILLING FILL is a solid color fill.
 * The two pairs of pitch and spacing control the fill or hatch if the fill type is FILLING MESH.
 * Only the first pair of pitch and spacing are used if the fill type is FILLING HATCH.

Example:
<pre>V 38000 67000 900 3 0 0 2 75 50 2 10 20 30 90 50</pre>

A circle with the center at (38000, 67000) and a radius of 900 mils,
color index 3, line width of 0 mils (smallest size), no cap, dashed line
type, dash length of 75 mils, dash spacing of 50 mils, mesh fill, 10
mils thick mesh lines, first mesh line: 20 degrees, with a spacing of
30 mils, second mesh line: 90 degrees, with a spacing of 50 mils.

### arc

Valid in: Schematic and Symbol files

Format: <pre>type x y radius startangle sweepangle color width capstyle dashstyle dashlength dashspace</pre>

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
		<td>A</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>Center X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>Center Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>radius</td>
		<td>int/mils</td>
		<td>Radius of the arc</td>
	</tr>
	<tr>
		<td>4</td>
		<td>startangle</td>
		<td>int/degrees</td>
		<td>Starting angle of the arc</td>
	</tr>
	<tr>
		<td>5</td>
		<td>sweepangle</td>
		<td>int/degrees</td>
		<td>Amount the arc sweeps</td>
	</tr>	
	<tr>
		<td>6</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>7</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of circle line</td>
	</tr>
	<tr>
		<td>8</td>
		<td>capstyle</td>
		<td>int</td>
		<td>Cap style</td>
	</tr>	
	<tr>
		<td>9</td>
		<td>dashstyle</td>
		<td>int</td>
		<td>Type of dash style</td>
	</tr>
	<tr>
		<td>10</td>
		<td>dashlength</td>
		<td>int/mils</td>
		<td>Length of dash</td>
	</tr>
	<tr>
		<td>11</td>
		<td>dashspace</td>
		<td>int/mils</td>
		<td>Space inbetween dashes</td>
	</tr>	
</table>

 * The startangle can be negative, but not recommended.
 * The sweepangle can be negative, but not recommended.
 * The capstyle is an enumerated type:
  * END NONE = 0
  * END SQUARE = 1
  * END ROUND = 2
 * The dashstyle is an enumerated type:
  * TYPE SOLID = 0
  * TYPE DOTTED = 1
  * TYPE DASHED = 2
  * TYPE CENTER = 3
  * TYPE PHANTOM = 4
 * The dashlength parameter is not used for TYPE SOLID and TYPE DOTTED. This parameter should take on a value of -1 in these cases.
 * The dashspace parameter is not used for TYPE SOLID. This parameter should take on a value of -1 in these case.

Example:<pre>A 30600 75000 2000 0 45 3 0 0 3 75 50</pre>

An arc with the center at (30600, 75000) and a radius of 2000 mils, a
starting angle of 0, sweeping 45 degrees, color index 3, line width of
0 mils (smallest size), no cap, center line type, dash length of 75
mils, dash spacing of 50 mils.

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
	<tr>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
	</tr>
	<tr>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
	</tr>
</table>
