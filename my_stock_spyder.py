# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:14:40 2017

@author: QingqingXiaocao
"""

#reference[IMPORTANT] : the BeautifulSoup get the static html source contenet;
#  while the selenium webdriver get the runtime html content.
#https://stackoverflow.com/questions/17597424/how-to-retrieve-the-values-of-dynamic-html-content-using-python


# solution: selenium + beautifulsoup
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from pymongo import MongoClient

###get for currently , fiexed url
def get_today_money_in():
    ### get the Money INOUT Amount
    #img=soup.find_all('div',{"class":"title1"})
    #for tit in img:
    #    href=tit.find('h3')
    #    if(href):
    #        a=href.find(lambda tag: tag.name=='a')
    #        if a:
    #            print a
    ##            if u"资金流入流出" in a.text:
    ##                print a
    
    ret="0"
    driver = webdriver.Chrome()
    url2="http://data.eastmoney.com/zjlx/"
    driver.get(url2)
    html2=driver.page_source
    moneyInOutSoup = BeautifulSoup(html2)
    if moneyInOutSoup.find("span",{"id":"data_jlr"}):
        ret=moneyInOutSoup.find("span",{"id":"data_jlr"}).text
    
    driver.quit()
    return ret

def insert_into_mongo(json):
    client=MongoClient('127.0.0.1')
    if client.Stock.authenticate('xiaocao101','nihao101ok'):
        coll=client.Stock.AllTradeEveryDay
        id_d=coll.insert_one(json)
        #print id_d.inserted_id
        with open("insert_mongo_log.txt", 'w') as f:
            f.write("insert: "+id_d.inserted_id)
        
    
driver = webdriver.Chrome()
driver.get('http://quote.eastmoney.com/zs000001.html')

html = driver.page_source
soup = BeautifulSoup(html)

cont=soup.find('div',{"id":"qqgscont"})
#print cont

vals=[]
for h in cont.find_all('b'):
    vals.append(h.text)
   
inout=get_today_money_in()

#driver.close()
driver.quit()


#0:上证指数
#2：上证成交量
#3:上证涨
#4：上证平
#5：上证跌

#6 深证指数
#8 深证成交量
#9 深证涨
#10 深证平
#11 深证跌

#if len(vals)==12:
#    print '上证指数：',vals[0]
#    print '上证成交量:',vals[2].split()[1]
#    print '上证涨：',vals[3]
#    print '上证平：',vals[4]
#    print '上证跌：',vals[5]
#    print '深证指数：',vals[6]
#    print '深证成交量:',vals[8].split()[1]
#    print '深证涨：',vals[9]
#    print '深证平：',vals[10]
#    print '深证跌：',vals[11]
    
jsonstr={
        '_id':time.strftime("%Y%m%d"),
        'Date':time.strftime("%Y%m%d"),
        'SHIndex':vals[0],
     'SHDealAmount':vals[2].split()[1],
    'SHUp':vals[3],
    'SHFlat':vals[4],
   'SHDown':vals[5],
    'SZIndex':vals[6],
     'SZDealAmount':vals[8].split()[1],
    'SZUp':vals[9],
     'SZFlat':vals[10],
    'SZDown':vals[11],
    "AmountOffset":inout
        }

#print jsonstr
insert_into_mongo(jsonstr)


    