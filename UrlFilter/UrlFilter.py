class UrlFilter:
    def __init__(self, shouldNotVisit):
        self.shouldNotVisit = shouldNotVisit;

    def addNotVistUrl(self, urls):
        for url in urls:
            if self.isInShouldNotVisit(url):
                self.shouldNotVisit.append(urls);

    def isInShouldNotVisit(self, url):
        for connectUrl in self.shouldNotVisit:
            if url == connectUrl:
                return False;
        return True

    def filter(self, urls):
        filteredUrls = [];
        for url in urls:
            if self.isInShouldNotVisit(url) and (url != None):
                filteredUrls.append(url);
                self.shouldNotVisit.append(url);
        return filteredUrls;
