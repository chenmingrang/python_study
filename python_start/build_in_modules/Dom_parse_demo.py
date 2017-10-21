#
from xml.dom.minidom import parse, parseString, Node

#Return a Document from the given input. filename_or_file may be either a file name, or a file-like object

#获取摸个节点的所有属性节点
def get_node_attr(node):
    if node.nodeType == Node.ELEMENT_NODE and node.hasAttributes():
        attrs = node.attributes
        for i in range(attrs.length):
            print(attrs.item(i).name ,':', attrs.item(i).value )

def get_none_text_children(node):
    res_list = []
    for child in node.childNodes:
        if child.nodeType == Node.ELEMENT_NODE:
            res_list.append(child)
    return res_list
def get_none_text_first_child(node):
    for child in node.childNodes:
        if child.nodeType == Node.ELEMENT_NODE:
            return child



dom1 = parse('./country_data.xml')

data_source = open('./country_data.xml')

root1 = dom1.documentElement
print(root1.tagName)
children = root1.childNodes
for child in children:
    get_node_attr(child)

country_1_children = get_none_text_children(get_none_text_first_child(root1))
print(country_1_children)
for child in country_1_children:
    if child.nodeType == Node.ELEMENT_NODE and child.nodeName == 'neighbor':
        get_node_attr(child)
        break

print('*='*20 ,'getElementsByTagName', '*='*20)
country_list = root1.getElementsByTagName('country')
for country in country_list:
    attr_node = country.getAttributeNode('name')
    print(attr_node.name, attr_node.value)


dom2 = parse(data_source)
dom3 = parseString('<myxml>Some data<empty/> some more data</myxml>')
assert dom3.documentElement.tagName == 'myxml'

print(root1.getElementsByTagName('country')[0].toxml())
print(root1.getElementsByTagName('country')[0].toprettyxml(indent='',newl=''))

print('*='*20, 'create a Document by calling a method on a “DOM Implementation” object', '*='*20)
from xml.dom.minidom import getDOMImplementation

impl = getDOMImplementation()
newdoc = impl.createDocument(None, 'some_tag', None)
top_element = newdoc.documentElement
text = newdoc.createTextNode('Some textual content.')
top_element.appendChild(text)
tag1 = newdoc.createElement('tag1')
tag1.appendChild(newdoc.createTextNode('tag1 content'))
top_element.appendChild(tag1)

print(newdoc.toxml())


print('*='*20, 'a fairly realistic example of a simple program.', '*='*20)

import xml.dom.minidom

document="""\
<slideshow>
<title>Demo slideshow</title>
<slide><title>Slide title</title>
<point>This is a demo</point>
<point>Of a program for processing slides</point>
</slide>

<slide><title>Another demo slide</title>
<point>It is important</point>
<point>To have more than</point>
<point>one slide</point>
</slide>
</slideshow>
"""

dom = xml.dom.minidom.parseString(document)

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return "".join(rc)


def handleSlideshow(slideshow):
    print("<html>")
    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print("</html>")

def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)

def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])
    handlePoints(slide.getElementsByTagName("point"))

def handleSlideshowTitle(title):
    print("<title>%s</title>" % getText(title.childNodes))

def handleSlideTitle(title):
    print("<h2>%s</h2>" % getText(title.childNodes))

def handlePoints(points):
    print("<ul>")
    for point in points:
        handlePoint(point)
    print("</ul>")

def handlePoint(point):
    print("<li>%s</li>" % getText(point.childNodes))

def handleToc(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print("<p>%s</p>" % getText(title.childNodes))

handleSlideshow(dom)