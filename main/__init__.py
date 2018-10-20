import urllib.request
import codecs
import urllib.parse
import ssl
from pip._vendor.appdirs import unicode
from html.parser import HTMLParser
from string import Template
import re
from urllib.parse import urlparse

class LinkFilter:
    def __init__(self, links):
        self.links=links
    def Filter(self):
        linksTuple = (self.links);
        return linksTuple; 
                
context = ssl._create_unverified_context()
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
url = 'https://www.lazada.vn/'
parser= CustomHTMLParser();
f1=codecs.open('./testfile.txt', 'w+', 'utf-8');
f2=codecs.open('./orgfile.txt', 'w+', 'utf-8');
f3 = codecs.open('./link.txt', 'w+', 'utf-8');
f4 = codecs.open('./prefix.txt', 'w+', 'utf-8');
                 
with urllib.request.urlopen(url,None,200) as response:
   convertedHtml =response.read().decode('utf-8');
   f2.write(convertedHtml)
   parser.feed(convertedHtml);
   for link in parser.linkArray:
       url = urlparse(link);
       f1.writelines("{} \n".format(url.geturl()));
       f3.writelines("{} \n".format(url.netloc+url.path+url.params));

f1.close();
f2.close();
f3.close();
f4.close();
