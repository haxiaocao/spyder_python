# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:07:10 2017

@author: QingqingXiaocao
"""

# reference: http://cuiqingcai.com/2636.html
# office site: https://pythonhosted.org/pyquery/
# pyquey ajax : https://pythonhosted.org/pyquery/ajax.html

from pyquery import PyQuery as pq
from lxml import etree


#4种初始化方式
#字符串
#lxml.etree
#url
#file




doc=pq('<html></html>')
#doc=pq(etree.fromstring('<html></html>'))
#print doc
#doc=pq('http://www.baidu.com')
#print doc

#doc=pq(filename='hello.html')
#print doc.html()
#print type(doc)
#li=doc('li')
#print li.text()

#==============================================================================
# #####P在其自身上面直接改变；
# p=pq('<p id="hello" class="helloclass"/>')('p')
# #print p
# #print p.attr('id')
# #print p.attr('class')
# #print p.attr('id','class')
# #print p.attr('id','proeep')
# 
# print p.addClass('beautiful')
# print p.removeClass('helloclass')
# print p.css('font-size','16px')
# print p.css({'background-color':'yellow'})
# #print p.attr('iddd')
# print p.css('fff','33')
#==============================================================================

#=============================Dom操作========================================
# p=pq('<p id="hello" class="helloClass"></p>')('p')
# #print p.append(' check out  <a href="http://reddit.com/r/python"><span>reddit</span></a>')
# #print p.append('I love you so much, and so long ')
# d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
# p.append(d('#test'))
# print p
# print d
# d.empty()
# print 'output the d after the empty operation'
# print d
#==============================================================================

#=======================遍历===================================================
# doc=pq(filename='hello.html')
# lis=doc('li')
# #print lis
# #for li in lis.items():
# #    print li.html()
# 
# ### it is the same with the for Items.
# print lis.each(lambda e: e)
# 
#==============================================================================

#============================网页请求=============================================
# #print pq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'})
# #print pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True)
# 
#==============================================================================



























