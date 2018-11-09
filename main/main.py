from CrawlerController.CrawlerController import CrawlerController
from UrlLayer.UrlLayer import UrlLayer
import sys
import os

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
if __name__ == '__main__':
    try:
        url = ['http://vnexpress.net']
        seeder = seed(url);
        crawler = CrawlerController(seeder);
        crawler.controller();
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

