# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 20:53:22 2017

@author: QingqingXiaocao
"""

# beautifulsoup official site:http://beautifulsoup.readthedocs.org/zh_CN/latest
# beautifulsoup :http://cuiqingcai.com/1319.html

import bs4
from bs4 import BeautifulSoup
import re


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
#==============================================================================
# 
# #2) NavigableString(标签内部的内容)
# print soup.p.string
# print type(soup.p.string)
#==============================================================================

#==============================================================================
# #3) beautifulSoup Object ：一个文档的全部内容
# print type(soup.name)
# print soup.name
# print soup.attrs
#==============================================================================

#==============================================================================
# #4) Comment:特殊类型的NavigableString 对象->去掉注释
# print soup.a
# print soup.a.string
# print type(soup.a)
# print type(soup.a.string)
# 
# if type(soup.a.string)==bs4.element.Comment:
#     print "if Comment:" + soup.a.string
#==============================================================================
   
###遍历文档树：
#Contentes[直接子节点]
#children【直接子节点】
# descendants 【所有子节点】
# string [节点内容]
#strings,stripped_strings [多个内容]
#parent [父节点], parents[全部父节点]
#next_sibling, previous_sibling ,next_siblings,previous_siblings[兄弟节点]，
#next_element(s), previous_element(s)[前后节点：对于所有节点，不分层次]


#print soup.head.contents
#for child in soup.body.children: #children is listiterator
#    print child
#
#for child in soup.descendants:
#    print child
    
#print soup.head.string
#print soup.html.string

#for string in  soup.strings:
#    print repr(string)
#for string in  soup.stripped_strings:
#    print repr(string)   

#p=soup.p
#print p
#print p.parent.name

#content=soup.head.title.string
#for parent in content.parents:
#    print parent.name
#print soup.p.prev_sibling
#print soup.p.next_sibling.next_sibling

###搜索文档树
#find_all(name , attrs , recursive , text , **kwargs)【子节点】
#find
#find_parent(s)
#find_next_sibling(s)
#find_previous_sibling(s)
#find_all_next(), find_next
#find_all_previous,find_previous

#print soup.find_all('b')
#for tag in soup.find_all(re.compile('^b')):
#    print tag.name
#print soup.find_all(['a','b'])

#for tag in soup.find_all(True):
#    print tag.name
#    
#def has_class_but_no_id(tag):
#    return tag.has_attr('class') and not tag.has_attr('id')
#print soup.find_all(has_class_but_no_id)  

#print soup.find_all(id='link2')
#print soup.find_all(href=re.compile('elsie'))

##同时过滤tag的多个属性
#print soup.find_all(href=re.compile('elsie'),id='link1')
#print soup.find_all('a',class_='sister') #note: class_

#有些tag属性在搜索中不能使用，如 data-*属性
#可以使用字典 来解
#data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
##data_soup.find_all(data-foo="value")
#print data_soup.find_all(attrs={'data-foo':'value'})

#print soup.find_all(text='Elsie')
#print soup.find_all(text=['Tillie','Elsie','Lacie'])
#print soup.find_all(text=re.compile('Dormouse'))

##print soup.find_all('a',limit=2)
#print soup.html.find_all('title')
#print soup.html.find_all('title',recursive=False)


###CSS 选择器: select method
## select 返回 list,需要遍历
#print soup.select('title')
#print soup.select('a')

##CLASS name is sister(.(ClassName))
#print soup.select('.sister') 

### ID Name[#(idname)]
#print soup.select('#link1')

### 组合查找
#print soup.select('p #link1')

###属性查找 ['属性名[标签]']
#print soup.select('a[class="sister"]')
#print soup.select('a[href="http://example.com/elsie"]')
print soup.select('p a[href="http://example.com/elsie"]')


##另外有beautifulsoup的 增删改功能，这里省略了。







































    



















    


