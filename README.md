The Upverter Universal Format Converter
=======================================
A command line python anything-in anything-out file converter to go between the multitude of electrical circuit schematic file formats. This project was started by Alex Ray (ajray@ncsu.edu), on behalf of Upverter (http://upverter.com).


Folder Contents
---------------

* `core/` - All of the converter code
* `doc/` - Everything related to documentation
* `parser/` - All of the in code
* `test/` - A set of test files for each format
* `writer/` - All of the out code


Usage
---------------

```bash
./upconvert.py -i test.sch -f kicad -t json -o test.json

-i: input file
-f: from format
-t: to format
-o: output file
```


Where to Get Help
---------------

```bash
./upconvert.py -h
```


Supported Formats
---------------

  The converter started with support for KiCad. We have since been expanding it to support many of the popular open and closed source formats, as follows.
* KiCad
* Eagle (in development)
* gEDA (in development)
* Fritzing (in development)
* Altium (in development)


Format Wish List
---------------

  This is the list of formats we wish we supported, and will work on someday (hopefully soon!). We are looking for developers to help us so please ping us if you're interested!
* DXDesigner & PADs
* Alegro
* OrCad

More in the todo list [TODO.md](https://github.com/upverter/schematic-file-converter/blob/master/TODO.md).


The Concept
---------------

  To use an Upverter Open JSON export in another piece of software, you will need to convert it into that software's proprietary format. Likewise, to get your data out of another piece of software and import it into Upverter, you will also need to run their export through the converter. We are working to make this easier, but we will largely depend on community contribution and the participation of the other vendors.


Interchange Format Documentation
---------------

  The converter is based on the Upverter Open JSON Format fully documented at http://upverter.com/resources/open-json-format/. We hope that someday all of the major providers of schematic capture software will support interoperability with open formats like this one.
