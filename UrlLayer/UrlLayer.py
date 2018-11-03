'''
Created on Nov 3, 2018

@author: hieun
'''

class UrlLayer:
    '''
    classdocs
    '''
    url = '';
    orgUrl= '';
    layer = 0;

    def __init__(self, params):
        '''
        Constructor
        '''
        self.set_url(params[0]);
        self.set_orgUrl(params[1]);
        self.set_layer(params[2]);
    
    def set_url(self, url):
        self.url= url;
    def get_url(self):
        return self.url;
    def set_orgUrl(self, orgUrl):
        self.orgUrl= orgUrl;
    def get_orgUrl(self):
        return self.orgUrl;
    def set_layer(self,layer):
        self.layer = layer;
    def get_layer(self):
        return self.layer;