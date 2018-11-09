from html.parser import HTMLParser

class HtmlParser(HTMLParser):
    linkArray=[];
    isTitle = False;
    title = "";
    txtArray = [];
    isTxt= False;
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            for attr in attrs:
                if attr[0]=="href":
                    self.linkArray.append(attr[1])
        if tag=="title":
            self.isTitle = True
        if tag!="script":
            self.isTxt= True;
    def handle_data(self, data):
        if self.isTitle:
            self.title= data.strip()
            self.isTitle = False
        str = data.strip();
        if (str!='')and (self.isTxt):
            self.txtArray.append(str);
        self.isTxt = False;