import re


class NormalizeUrl:
    url = ""
    orgPrefix = ""

    def __init__(self, url, orgPrefix):
        self.url = url;
        self.orgPrefix = orgPrefix;
        
    def removeVoid(self):
        regex = re.compile('(void)+')
        if re.match(regex,self.url):
            return "";
        return self.url;

    def trimUrl(self):
        return self.url.strip();
    
    def removeWorlWideWeb(self):
        regexCheckHead = re.compile("(www.)+");
        if (self.url != "") and (self.url != None):
            if regexCheckHead.match(self.url):
                return "http://" + self.url[4:];
            else:
                return "http://" + self.url;

        return self.url;

    def appendPrefix(self):
        if self.url != "":
            if (self.url[0] == '/'):
                return self.orgPrefix + self.url;
        return self.url;
    
    def removeBackSlash(self):
        lastCharacter =len(self.url)-1;
        if lastCharacter>=0:
            if self.url[lastCharacter] =="/":
                return self.url[:lastCharacter]
            return self.url
        return self.url;
    
    def convertUrl(self):
        self.url = self.removeVoid()
        self.url = self.trimUrl()
        self.url = self.removeBackSlash();
        self.url = self.appendPrefix();
        self.url = self.removeWorlWideWeb();
        return self.url
