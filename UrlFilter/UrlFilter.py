class UrlFilter:
    def __init__(self, shouldNotVisit):
        self.shouldNotVisit = shouldNotVisit;

    def addNotVistUrl(self, urls):
        for url in urls:
            if self.isInShouldNotVisit(url):
                self.shouldNotVisit.append(urls);

    def isInShouldNotVisit(self, url):
        if url in self.shouldNotVisit:
            return True
        return False



    def filter(self, urls):
        filteredUrls = [];
        for url in urls:
            if self.isInShouldNotVisit(url)==False and (url != None):
                filteredUrls.append(url);
                self.shouldNotVisit.append(url)
        return filteredUrls;

    def addShoudlNotVisit(self,url):
        if self.isInShouldNotVisit(url)==False:
            self.shouldNotVisit.append(url)
            
    def getSoundNotVisitList(self):
        return self.shouldNotVisit