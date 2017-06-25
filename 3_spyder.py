# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:14:17 2017

@author: QingqingXiaocao
"""

#reference: 
   
#    http://cuiqingcai.com/2443.html
#    https://github.com/binux/pyspider
#    http://docs.pyspider.org/en/latest/

#START RUN IN COMMAND LINE :  pyspider all

##NOTE: you should use python 32bit version to use the pyspider.

from pyspider.libs.base_handler import *

class Handle(BaseHandler):
    crawl_config={}
    
    def __init__(self):
        self.base_url="https://mm.taobao.com/json/request_top_list.htm?page="
        self.page_num=1
        self.total_num=30
        
    @every(minutes=24*60)
    def on_start(self):
        while self.page_num<=self.total_num:
            url=self.base_url+str(self.page_num)
            print url
            self.crawl(url,callback=self.index_page)
            self.page_num+=1
    
    @config(age=10*24*60*60)    
    def index_page(self,response):
        for each in response.doc('a[href^="http"]').items():
            self.craw(each.attr.href,callback=self.detail_page)
    
    @config(priority=2)     
    def detail_page(self,response):
        return {
            'url':response.url,
            'title':response.doc('title').text(),
                }
        
            