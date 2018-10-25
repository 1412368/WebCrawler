from html.parser import HTMLParser

class LinkGetter(HTMLParser):
    linkArray=[];
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            for attr in attrs:
                if attr[0]=="href":
                    self.linkArray.append(attr[1])
