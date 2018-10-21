import urllib.request
import codecs
import urllib.parse
from pip._vendor.appdirs import unicode
from html.parser import HTMLParser
from string import Template
import re
from urllib.parse import urlparse
from multiprocessing import Queue
from threading import Thread
from _collections import deque
from NormalizeUrl import NormalizeUrl
from threading import Timer

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
                    

data=[];
url = 'https://lazada.vn'
parser= CustomHTMLParser();
f1=codecs.open('./testfile.txt', 'w+', 'utf-8');
f2=codecs.open('./orgfile.txt', 'w+', 'utf-8');
f3 = codecs.open('./link.txt', 'w+', 'utf-8');
f4 = codecs.open('./queueURl.txt', 'w+', 'utf-8');
f5 = codecs.open('./connectError.txt', 'w+', 'utf-8');

def getLinkFromPage(url):
    parsedUrl = urlparse(url);        
    try: 
        with urllib.request.urlopen(url,None,200) as response:
            convertedHtml =response.read().decode('utf-8');
            f2.write(convertedHtml)
            parser.feed(convertedHtml);
            normalizedUrls = [];
            for link in parser.linkArray:
                url = urlparse(link);       
                f1.writelines("{} \n".format(url.geturl()));
                fullUrl= url.netloc+url.path+url.params;
                if (fullUrl !="")and (fullUrl !=None):
                    normalizeUrl = NormalizeUrl(fullUrl,parsedUrl.netloc)
                    fullUrl = normalizeUrl.convertUrl();
                    f3.writelines("{} \n".format(fullUrl));
                    normalizedUrls.append(fullUrl);
            return normalizedUrls;
    except :
        print("ValueError");
        print(url);
        f5.writelines("{} \n".format(url));
        return []
def checkDuplicateUrl(connectQueue, url):
    for connectUrl in connectQueue:
        if url == connectUrl:
            return False;
    return True
    
def addUrlToConnectQueue(connectQueue, urlArray):
    for url in urlArray:
        if checkDuplicateUrl(connectQueue, url) and (url!=None):
            connectQueue.append(url);

def controller(connectQueue):
#     while len(connectQueue)>0:
    for i in range(0,10):
        url = connectQueue.popleft();
        urlArray= getLinkFromPage(url);
        r = Timer(1.0, addUrlToConnectQueue(connectQueue, urlArray));
        for url in connectQueue:
            f4.writelines("{}\n".format(url))
        f4.writelines("--------------------------------------------\n")
        
connectQueue = deque([url]);
controller(connectQueue);
f1.close();
f2.close();
f3.close();
f4.close();
f5.close();