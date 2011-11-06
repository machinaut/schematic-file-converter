import xml.etree.ElementTree as et

class eagleSchematic:
  def __init__(self, file_path):
    xml_contents = et.ElementTree()
    xml_contents.parse(file_path)
    self.json_contents
if __name__ == "__main__":
  sch = et.ElementTree()
  sch.parse('./mintyboostv3.sch')
  for thing in sch.getiterator():
    print dict({thing.tag:thing.attrib})
