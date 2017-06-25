# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 07:43:11 2017

@author: QingqingXiaocao
"""
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
#import requests
import urllib2

#r = requests.get(r"http://quote.eastmoney.com/zs000001.html")
##print r.text
#soup=BeautifulSoup(r.text)
#
###print soup.prettify()
##for child in soup.body.children:
##    print child
#
#gl=soup.select('#qqgscont')
##print type(gl[0])
#
#lable=soup.select("div #qqgscont")
##print type(lable[0])
##print lable[0].name
##print lable[0].attrs
#print lable
#
#for i in lable:
#    print type(i.name)
#    print "----------------\n"
#    
    
##htmlCharset = "utf-8";
#htmlCharset = "gb2312";
#url = 'http://quote.eastmoney.com/zs000001.html'
url='http://quote.eastmoney.com/center/list.html#10_0_0_u?sortType=C&sortRule=-1'
#resp = requests.get(url)
#soup = BeautifulSoup(resp.text, 'lxml',fromEncoding=htmlCharset)
#
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html,'html5lib')


cont=soup.find('div',{"id":"qqgscont"})
print cont.prettify()

#urls = []
for h in cont.find_all('li'):
    print '3'
    print "=======================",h.text
#    a = h.find('id')
#    urls.append(a.attrs['href'])




#opener = urllib2.build_opener()
#opener.addheaders = [('User-agent', 'Mozilla/5.0')]
#data = opener.open(url).read()
#soup=BeautifulSoup(data,'html.parser')
#cont=soup.find('div',{"id":"qqgscont"})
#print cont
#
##urls = []
#for h in cont.find_all('a'):
#    print '2'
#    print "=======================",h.text


html = urllib2.urlopen(url).read()
bs = BeautifulSoup(html)
table = bs.find(lambda tag: tag.name=='table' and tag.has_key('id') and tag['id']=="Table1") 
rows = table.findAll(lambda tag: tag.name=='tr')




