# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 17:27:50 2017

@author: QingqingXiaocao
"""
#python IDE - Spyder常用快捷键 
#==============================================================================
# http://blog.csdn.net/tiffanyrabbit/article/details/69257453
#==============================================================================
#reference: http://cuiqingcai.com/968.html

import urllib2
import cookielib

cookie=cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
#创建更一般的opener来实现对Cookie的设置。
opener=urllib2.build_opener(handler)

response=opener.open('http://www.baidu.com')
for item in cookie:
    print 'name=' + item.name
    print 'value='+item.value
    

#==============================================================================
#     # use the cookie to login and get some data from file of cookie.
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib2.urlencode({
#             'stuid':'201200131012',
#             'pwd':'23342321'
#         })
# #登录教务系统的URL
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# #模拟登录，并把cookie保存到变量
# result = opener.open(loginUrl,postdata)
# #保存cookie到cookie.txt中
# cookie.save(ignore_discard=True, ignore_expires=True)
# #利用cookie请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# #请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print result.read()
#==============================================================================
