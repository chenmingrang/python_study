"""
操作XML有两种方法：DOM和SAX。
DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
正常情况下，优先考虑SAX，因为DOM实在太占内存。
在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
"""
"""
example当SAX解析器读到一个节点时:
    <a href="/">python</a>
会产生3个事件：
1.start_element事件，在读取<a href="/">时；
2.char_data事件，在读取python时；
3.end_element事件，在读取</a>时。
"""

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        end_ele = name
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


print("*="*10, 'demo', "*="*10)

import re
class WeatherSaxHandler(object):

    def __init__(self, result):
        self.result = result
        self._today = 0
        self._count = 0

    def start_element(self, name, attrs):
        if name == "yweather:location":
            self.result['city'] = attrs['city']
            self.result['country'] = attrs['country']
        if name == "yweather:condition":
            date_arr =  re.split(r'[\s,]+', attrs['date'])[1:4]
            self.today = " ".join(date_arr)
        if name == "yweather:forecast":
            self._count += 1
            if self.today == attrs['date']:
                self.result["today"] = {}
                self.result["today"]["text"] = attrs["text"]
                self.result["today"]["low"]= attrs["low"]
                self.result["today"]["high"] = attrs["high"]
            if self._count == 2:
                self.result["tomorrow"] = {}
                self.result["tomorrow"]["text"] = attrs["text"]
                self.result["tomorrow"]["low"] = attrs["low"]
                self.result["tomorrow"]["high"] = attrs["high"]

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass

def parse_weather(file_path):
    result = {}
    handler = WeatherSaxHandler(result)
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    f = open(file_path, 'rb')
    parser.ParseFile(f)
    return result

print(parse_weather('./weather.xml'))