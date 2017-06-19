# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 20:53:22 2017

@author: QingqingXiaocao
"""

# beautifulsoup official site:http://beautifulsoup.readthedocs.org/zh_CN/latest
# beautifulsoup :http://cuiqingcai.com/1319.html

from bs4 import BeautifulSoup


#==============================================================================
html = """
 <html><head><title>The Dormouse's story</title></head>
 <body>
 <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
 <p class="story">Once upon a time there were three little sisters; and their names were
 <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
 <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
 <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
 and they lived at the bottom of a well.</p>
 <p class="story">...</p>
 """
 
soup=BeautifulSoup(html)
# # 格式化输出，经常用到
# print soup.prettify()
#==============================================================================

##BeautifulSoup 将HTML四大对象种类
#(1)Tag
#(2)NavigableString
#(3)BeautifulSoup
#(4)Comment

#==============================================================================
# #1) Tag
# # in this way ,it will get the first one taga
# 
# #print soup.title
# #print soup.head
# #print soup.a
# #print soup.p
# #print type(soup.head)
# #
# ## two important attributes
# #print soup.name
# #print soup.head.name
# #print soup.p.attrs  # print p all attributes
# 
# print soup.p['class']
# soup.p['class']='modify class'
# print soup.p['class']
# 
# print soup.p
# del soup.p['class']
# print soup.p
# 
# 
#==============================================================================

#2) NavigableString






