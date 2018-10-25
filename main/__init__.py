import CrawlerController
from _collections import deque
import codecs
class LinkFilter:
    def __init__(self, links):
        self.links=links
    def Filter(self):
        linksTuple = (self.links);
        return linksTuple; 
                
                    

data=[];
url = 'https://lazada.vn'
        
connectQueue = deque([url]);
crawler = CrawlerController.CrawlerController(connectQueue);

crawler.controller();