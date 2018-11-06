import urllib.request
import codecs
import urllib.parse
from pip._vendor.appdirs import unicode
from html.parser import HTMLParser
from string import Template
import re
from urllib.parse import urlparse
from _collections import deque
from NormalizeUrl.NormalizeUrl import NormalizeUrl
from threading import Timer
from UrlFilter.UrlFilter import UrlFilter
from HtmlParser.HtmlParser import HtmlParser
from UrlLayer.UrlLayer import UrlLayer
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
class CrawlerController:
    f1 = codecs.open('./testfile.txt', 'w+', 'utf-8');
    f2 = codecs.open('./orgfile.txt', 'w+', 'utf-8');
    f3 = codecs.open('./link.txt', 'w+', 'utf-8');
    f4 = codecs.open('./queueURl.txt', 'w+', 'utf-8');
    f5 = codecs.open('./connectError.txt', 'w+', 'utf-8');

    parser = HtmlParser();
    connectQueue = deque([]);
    urlFilter = UrlFilter([]);
    def __init__(self, connectQueue):
        self.connectQueue = connectQueue;

    def appendToQueue(self, urls):
        for url in urls:
            self.connectQueue.append(url);

    def createLayerList(self, urls, layer):
        layerList= [];
        for url in urls:
            parsedUrl = urlparse(url);
            urlLayer = UrlLayer([url,parsedUrl.netloc, layer]);
            layerList.append(urlLayer)
        return layerList;
        
    def createConnection(self):
        if len(self.connectQueue)>0:
            urlLayer = self.connectQueue.popleft();
            url = urlLayer.get_url();
            layer= urlLayer.get_layer();
            html = self.getHtmlFromLink(url);
            self.urlFilter.addShoudlNotVisit(url)
            urls = self.getLinkFromPage(html, url);
            filteredUrl = self.urlFilter.filter(urls);
            layerList = self.createLayerList(filteredUrl,layer+1);
            self.appendToQueue(layerList);

    def getHtmlFromLink(self, url):
        print("connecting {} ...".format(url))
        if self.urlFilter.checkRobots(url):
            try:
                with urllib.request.urlopen(url, None, 200) as response:
                    convertedHtml = response.read().decode('utf-8');
                    return convertedHtml;
            except ValueError:
                print(ValueError);
                self.f5.writelines("{} \n".format(url));
                return None

    def getLinkFromPage(self, html, orgUrl):
        parsedUrl = urlparse(orgUrl.strip());
        if html != None:
            self.f2.write(html)
            self.parser.feed(html);
        normalizedUrls = [];
        for link in self.parser.linkArray:
            url = urlparse(link.strip());
            self.f1.writelines("{} \n".format(url.geturl()));
            fullUrl = url.netloc + url.path + url.params;
            if (fullUrl != "") and (fullUrl != None):
                normalizeUrl = NormalizeUrl(fullUrl, parsedUrl.netloc)
                fullUrl = normalizeUrl.convertUrl();
                self.f3.writelines("{} \n".format(fullUrl));
                normalizedUrls.append(fullUrl);
        return normalizedUrls;

    def controller(self):
        #     while len(connectQueue)>0:
        for i in range(0, 10):
            r = Timer(1.0, self.createConnection());
            for url in self.connectQueue:
                self.f4.writelines("{}\n".format(url.url))
            self.f4.writelines("--------------------------------------------\n")
        self.f1.close();
        self.f2.close();
        self.f3.close();
        self.f4.close();
        self.f5.close();
