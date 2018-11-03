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
                
    def checkOrgUrlWithNewUrl(self, newUrl):
        parsedNewUrl = urlparse(newUrl);
        if (self.orgUrl != parsedNewUrl.netloc) and (parsedNewUrl.netloc!=""):
            self.orgUrl= parsedNewUrl.netloc;
            normalizedUrl= NormalizeUrl(self.orgUrl,self.orgUrl);
            normalized = normalizedUrl.convertUrl();
            self.robotsParser.set_url(normalized+"/robots.txt");
            try:
                self.robotsParser.read();
            except ValueError:
                print("can't connect")
    def robotsFilter(self, url):
        return self.robotsParser.can_fetch('*',url);    
    
    def isInShouldNotVisit(self, url):
        if url in self.shouldNotVisit:
            return True
        return False

    def filter(self, urls):
        filteredUrls = [];
        for url in urls:
            self.checkOrgUrlWithNewUrl(url);
            if self.isInShouldNotVisit(url)==False and (url != None) and self.robotsFilter(url):
#             if self.isInShouldNotVisit(url)==False and (url != ""):
                filteredUrls.append(url);
                self.shouldNotVisit.append(url)
        return filteredUrls;

    def addShoudlNotVisit(self,url):
        if self.isInShouldNotVisit(url)==False:
            self.shouldNotVisit.append(url)
            
    def getSoundNotVisitList(self):
        return self.shouldNotVisit