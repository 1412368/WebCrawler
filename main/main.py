from CrawlerController.CrawlerController import CrawlerController
from UrlLayer.UrlLayer import UrlLayer
from _collections import deque
import codecs


class LinkFilter:
    def __init__(self, links):
        self.links = links

    def Filter(self):
        linksTuple = (self.links);
        return linksTuple;

def seed(urlSeed):
    seedArray=[];
    for url in urlSeed:
        urlLayer = UrlLayer([url,url,0]);
        seedArray.append(urlLayer);
    return seedArray;

data = [];
url = 'http://tiki.vn'
data.append(url)
seeder = seed(data);
connectQueue = deque(seeder);
crawler = CrawlerController(connectQueue);

crawler.controller();