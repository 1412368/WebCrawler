import urllib.request
import codecs
import urllib.parse
import ssl
from pip._vendor.appdirs import unicode
from html.parser import HTMLParser
from string import Template
import re

context = ssl._create_unverified_context()
class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            for attr in attrs:
                if attr[0]=="href":
                    f1.writelines("attribute:{} \n" .format(attr[1]))

#     def handle_endtag(self, tag):
#         f1.writelines("Encountered a end tag:%s \n" %(tag))

#     def handle_data(self, data):
#         f1.writelines("Encountered some data  :%s \n" %(data))
data=[];
url = 'https://tiki.vn/'
parser= CustomHTMLParser();
f1=codecs.open('./testfile.txt', 'w+', 'utf-8');
f2=codecs.open('./orgfile.txt', 'w+', 'utf-8');

with urllib.request.urlopen(url,context=context) as response:
   convertedHtml =response.read().decode('utf-8');
   f2.write(convertedHtml)
   parser.feed(convertedHtml);
