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

dom2 = parse(data_source)

dom3 = parseString('<myxml>Some data<empty/> some more data</myxml>')

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

from xml.dom.minidom import getDOMImplementation

impl = getDOMImplementation()

newdoc = impl.createDocument(None, 'some_tag', None)
top_element = newdoc.documentElement
text = newdoc.createTextNode('Some textual content.')
top_element.appendChild(text)


