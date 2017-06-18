# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 15:03:15 2017

@author: QingqingXiaocao
"""


# reference : http://cuiqingcai.com/977.html

#==============================================================================
# #返回pattern对象
# re.compile(string[,flag])  
# #以下为匹配所用函数
# re.match(pattern, string[, flags])
# re.search(pattern, string[, flags])
# re.split(pattern, string[, maxsplit])
# re.findall(pattern, string[, flags])
# re.finditer(pattern, string[, flags])
# re.sub(pattern, repl, string[, count])
# re.subn(pattern, repl, string[, count])
#==============================================================================

#==============================================================================
# pattern=re.compile(r'hello')
# result1=re.match(pattern,'helloww')
# result2=re.match(pattern,'heo')
# 
# if result1:
#     print result1.group()
# else:
#     print "match is wrong"
#     
# if result2:
#     print result2.group()
# else:
#     print 'result 2 is not match:'
#==============================================================================
    
#==============================================================================
# m=re.match(r'(\w+) (?P<num2>\w+)(?P<sign>.*)', 'hello world!')
# 
# print "m.string:", m.string
# print "m.re:", m.re
# print "m.pos:", m.pos
# print "m.endpos:", m.endpos
# print "m.lastindex:", m.lastindex
# print "m.lastgroup:", m.lastgroup
# print "m.group():", m.group()
# print "m.group(1,2):", m.group(1, 2)
# print "m.groups():", m.groups()
# print "m.groupdict():", m.groupdict()
# print "m.start(2):", m.start(2)
# print "m.end(2):", m.end(2)
# print "m.span(2):", m.span(2)
# print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')
# 
#==============================================================================

#==============================================================================
# pattern=re.compile(r'world')
# search=re.search(pattern,'hellor world')
# 
# 
# if search:
#     print "search is matching:",match.group()
#    
# match=re.match(pattern, 'hello world')
# if match:
#     "Match method:",match.group()
# else:
#     print "match is not right."
#==============================================================================
#==============================================================================
# 
# pattern=re.compile(R'\d+')
# print re.split(pattern,'one1two2three3four4')
#==============================================================================
#==============================================================================
# 
# pattern=re.compile(r'\d+')
# print re.findall(pattern,'one1two2three3four4')
#==============================================================================

#==============================================================================
# # finditer is used for iterating the collections.
# pattern=re.compile(r'\d+')
# for m in re.finditer(pattern,'one1two2three3four4'):
#     print m.group()
# 
#==============================================================================

#==============================================================================
# pattern=re.compile(r'(\w+) (\w+)')
# stri='I say, hello world!'
# 
# print re.sub(pattern,r'\2 \1',stri)
# 
# def func(m):
#     return m.group(1).title() + ' '+ m.group(2).title()
#     
# print re.sub(pattern,func,stri)
#==============================================================================

#==============================================================================
# pattern=re.compile(r'(\w+) (\w+)')
# stri='I say, hello world!'
#  
# print re.subn(pattern,r'\2 \1',stri,count=1)
#==============================================================================




