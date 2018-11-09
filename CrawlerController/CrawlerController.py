import urllib.request
import codecs
import urllib.parse
import threading
from urllib.parse import urlparse
import queue
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

    urlFilter = UrlFilter([]);
    def __init__(self, seeder):
        self.connectQueue = queue.Queue();
        for item in seeder:
            self.connectQueue.put(item)
    def appendToQueue(self, urls):
        for url in urls:
            self.connectQueue.put(url);

    def createLayerList(self, urls, layer):
        layerList= [];
        for url in urls:
            parsedUrl = urlparse(url);
            urlLayer = UrlLayer([url,parsedUrl.netloc, layer]);
            layerList.append(urlLayer)
        return layerList;
        
    def createConnection(self,urlLayer):
        url = urlLayer.get_url();
        layer= urlLayer.get_layer();
        html = self.getHtmlFromLink(url);
        self.urlFilter.addShoudlNotVisit(url);
        parser = HtmlParser();
        if html!=None:
            parser.feed(html);
            urls = self.getLinkFromPage(html, url,parser);
#       must run getLinkFromPage before
            title = parser.title;
            if title!= "":
                htmlFile = codecs.open('./storageFolder/'+title+'.html', 'w+', 'utf-8');
                txtFile = codecs.open('./storageFolder/'+title+'.txt', 'w+', 'utf-8');
                htmlFile.write(html);
                for text in parser.txtArray:
                    txtFile.write(text);
                htmlFile.close();
                txtFile.close();
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
    
    def getLinkFromPage(self, html, orgUrl,parser):
        parsedUrl = urlparse(orgUrl.strip());
        normalizedUrls = [];
        for link in parser.linkArray:
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
        while(not self.connectQueue.empty()):
            threadList=[]
            while (threading.activeCount() < 8):
                if not self.connectQueue.empty():
                    urlLayer = self.connectQueue.get();
                    t = threading.Thread(target=self.createConnection, args=[urlLayer])
                    t.start()
                    threadList.append(t)
                    print("queue length {}".format(self.connectQueue.qsize()))
            for i in threadList:
                i.join()
        # for i in range(0, 10):
        #     r = Timer(1.0, self.createConnection());
            # for url in self.connectQueue:
            #     self.f4.writelines("{}\n".format(url.url))
            # self.f4.writelines("--------------------------------------------\n")
        # self.f1.close();
        # self.f2.close();
        # self.f3.close();
        # self.f4.close();
        # self.f5.close();
