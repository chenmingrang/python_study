"""
The XML handling submodules are:

xml.etree.ElementTree: the ElementTree API, a simple and lightweight XML processor
xml.dom: the DOM API definition
xml.dom.minidom: a minimal DOM implementation
xml.dom.pulldom: support for building partial DOM trees
xml.sax: SAX2 base classes and convenience functions
xml.parsers.expat: the Expat parser binding
"""
print("*="*20, 'ET', "*="*20)
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
#root = ET.fromstring(country_data_as_string)
print(root.tag)#data
print(type(root))#<class 'xml.etree.ElementTree.Element'>
print(root.attrib)
for child in root:
    print(child.tag, ':', child.attrib)
print(root[0][1].text)#2008

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)


for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print('country = %s ;rank = %s' % (name, rank))

#Modifying an XML File
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('country_data_updated.xml')

#remove element from xml
for country in root.iter('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('country_data_rm.xml')



#Building XML documents
print('*='*20, 'Building XML documents', '*='*20)
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
f = ET.Element('f')
f.set('name', 'f_tag')
a.append(f)
ET.dump(a)


#Parsing XML with Namespaces
print('*='*20, 'Parsing XML with Namespaces', '*='*20)
xml_text = r"""<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>
"""

root = ET.fromstring(xml_text)
ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print(name.text)
    for char in actor.findall('role:character', ns):
        print(' |-->', char.text)


# XPath support
print('*=' * 20, 'XPath support', '*=' * 20)
tree = ET.parse('country_data.xml')
root = tree.getroot()

#Top-level elements
print(root.findall(".")[0].tag)#data

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
for neighbor in root.findall("./country/neighbor"):
    print("name=%s direction=%s" % (neighbor.get("name"), neighbor.get("direction")))

# Nodes with name='Singapore' that have a 'year' child
ele = root.findall(".//year/..[@name='Singapore']")
print(ele[0].get('name'))

# 'year' nodes that are children of nodes with name='Singapore'
ele = root.findall(".//*[@name='Singapore']/year")
print(ele[0].text)
# All 'neighbor' nodes that are the second child of their parent
ele = root.findall(".//neighbor[2]")
for e in ele:
    print(e.get("name"))



#非阻塞解析
print('*='*20, '非阻塞', '*='*20)
parser = ET.XMLPullParser(['start', 'end'])
parser.feed('<mytag>sometext')
print(list(parser.read_events()))
parser.feed(' more text</mytag>')
for event, ele in parser.read_events():
    print(event)
    print(ele.tag, 'text=', ele.text)

