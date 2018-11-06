from HtmlParser.HtmlParser import HtmlParser
import urllib.robotparser
from urllib.parse import urlparse
from NormalizeUrl.NormalizeUrl import NormalizeUrl
import re
class UrlFilter:
    
    def __init__(self, shouldNotVisit):
        self.shouldNotVisit = shouldNotVisit;
        self.robotsParser = urllib.robotparser.RobotFileParser();
        self.orgUrl = '';
    
    def addNotVistUrl(self, urls):
        for url in urls:
            if self.isInShouldNotVisit(url):
                self.shouldNotVisit.append(urls);
                
    def checkRobots(self, newUrl):
        parsedNewUrl = urlparse(newUrl);
        if (self.orgUrl != parsedNewUrl.netloc) and (parsedNewUrl.netloc!=""):
            normalizedUrl= NormalizeUrl(parsedNewUrl.netloc,parsedNewUrl.netloc);
            normalized = normalizedUrl.convertUrl();
            try:
                urllib.request.urlopen(normalized+"/robots.txt", None, 200)
            except IOError as e :
                print(e);
                return False;
            try:
                self.robotsParser.set_url(normalized+"/robots.txt");
                self.robotsParser.read();
                self.orgUrl= parsedNewUrl.netloc;
            except IOError:
                print(self.orgUrl);
                print(IOError);
                print("can't connect")
                return False;
        return self.robotsParser.can_fetch('*',newUrl);            
    
    def isInShouldNotVisit(self, url):
        if url in self.shouldNotVisit:
            return True
        return False

    def filter(self, urls):
        filteredUrls = [];
        for url in urls:
            if self.isInShouldNotVisit(url)==False and (url != None):
#             if self.isInShouldNotVisit(url)==False and (url != ""):
                filteredUrls.append(url);
                self.shouldNotVisit.append(url)
        return filteredUrls;

    def addShoudlNotVisit(self,url):
        if self.isInShouldNotVisit(url)==False:
            self.shouldNotVisit.append(url)
            
    def getSoundNotVisitList(self):
        return self.shouldNotVisit