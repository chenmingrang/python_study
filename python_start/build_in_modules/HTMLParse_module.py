#HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML

#Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
print("*="*5, 'Parsing a doctype:', "*="*5)
parser.feed(r'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">''')

print("*="*5, 'Parsing an element with a few attributes and a title:', "*="*5)
parser.feed('<img src="python-logo.png" alt="The Python logo">')
parser.feed('<h1>Python</h1>')

print("*="*5, 'The content of script and style elements is returned as is, without further parsing:', "*="*5)
parser.feed('<style type="text/css">#python { color: green }</style>')
parser.feed(r"""<script type="text/javascript">alert("<strong>hello!</strong>");</script>""")

print("*="*5, 'Parsing comments:', "*="*5)
parser.feed(r"""<!-- a comment --><!--[if IE 9]>IE-specific content<![endif]-->""")

print("*="*5, r'''Parsing named and numeric character references and converting them to the correct char (note: these 3 references are all equivalent to '>'):''', "*="*5)
parser.feed(r'''<p>&gt; &#62; &#x3E;</p>''')


print("*="*5,'Feeding incomplete chunks to feed() works, but handle_data() might be called more than once (unless convert_charrefs is set to True):', "*="*5)
for chunk in ['<sp', 'an>buff', 'ered ', 'test</s', 'pan>']:
    parser.feed(chunk)

print("*="*5, 'Parsing invalid HTML (e.g. unquoted attributes) also works:', "*="*5)
parser.feed('<p><a class=link href=#main>tag soup</p ></a>')