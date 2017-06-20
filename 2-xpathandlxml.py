# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 07:41:26 2017

@author: QingqingXiaocao
"""

#reference : http://cuiqingcai.com/2621.html
#lxml official site: http://lxml.de/index.html

#lxml 的使用
from lxml import etree

#==============================================================================
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# # add html, body tag automatically.
# result = etree.tostring(html)
# print(result)
# 
#==============================================================================

#html=etree.parse('hello.html')
#result=etree.tostring(html,pretty_print=True)
#print result

html=etree.parse('hello.html')
#print type(html)
#result=html.xpath('//li')
#print result
#print type(result)
#print result[0]

## get teh attribute:
#result=html.xpath('//li/@class')
#print result

#result=html.xpath('//li/a[@href="link1.html"]')
#print result
#print type(result)

##获取 <li> 标签下的所有 <span> 标签
#result=html.xpath('//li/span')
#print result
#result=html.xpath('//li//span')  #use this 
#print result

result=html.xpath('//li/a//@class')
result=html.xpath('//li[last()]/a/@href')
result=html.xpath('//li[last()-1]/a')
result=html.xpath('//*[@class="bold"]')
print result
print result[0].text





