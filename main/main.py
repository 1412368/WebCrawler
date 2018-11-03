from CrawlerController.CrawlerController import CrawlerController
from _collections import deque
import codecs


class LinkFilter:
    def __init__(self, links):
        self.links = links

    def Filter(self):
        linksTuple = (self.links);
        return linksTuple;


data = [];
url = 'https://lazada.vn'
data.append(url)
connectQueue = deque(data);
crawler = CrawlerController(connectQueue);

crawler.controller();