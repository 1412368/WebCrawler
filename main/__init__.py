import urllib.request
import codecs
import urllib.parse
from pip._vendor.appdirs import unicode
from html.parser import HTMLParser
from string import Template
import re

class LinkFilter:
    def __init__(self, links):
        self.links=links
    def Filter(self):
        linksTuple = (self.links);
        return linksTuple; 
                
class CustomHTMLParser(HTMLParser):
    linkArray=[];
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            for attr in attrs:
                if attr[0]=="href":
                    self.linkArray.append(attr[1])

#     def handle_endtag(self, tag):
#         f1.writelines("Encountered a end tag:%s \n" %(tag))

#     def handle_data(self, data):
#         f1.writelines("Encountered some data  :%s \n" %(data))
data=[];
url = 'https://tiki.vn/'
parser= CustomHTMLParser();
f1=codecs.open('./testfile.txt', 'w+', 'utf-8');
f2=codecs.open('./orgfile.txt', 'w+', 'utf-8');
f3 = codecs.open('./link.txt', 'w+', 'utf-8');
                 
with urllib.request.urlopen(url,None,2000) as response:
   convertedHtml =response.read().decode('utf-8');
   f2.write(convertedHtml)
   parser.feed(convertedHtml);
   for link in parser.linkArray:
        f3.writelines("{} \n".format(link) );