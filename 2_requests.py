# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:37:36 2017

@author: QingqingXiaocao
"""

# official site API: http://docs.python-requests.org/en/master/api/
# reference: http://cuiqingcai.com/2556.html

#The Content: 
#1 get method 
#2 post request method  
#3  Cookies
#4 timeout settings 
#5  Session 会话对象
#6  SSL vertificate file
#7  Proxy 代理

import requests
import json

#==============================================================================
# r=requests.get('http://cuiqingcai.com')
# print type(r)
# print r.status_code
# print r.encoding
# print r.cookies
# print r.text
#==============================================================================

#==============================================================================
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")
#==============================================================================

# 1 get method
#==============================================================================
#r=requests.get("http://httpbin.org/get")
#payload={'key1':'value1','key2':'value2'}
#headers={'content-type':'application/json'}
#r=requests.get("http://httpbin.org/get",params=payload)
#print r.url
# print r.text
# print r.json()
# print r.raw
#==============================================================================

#==============================================================================
# #2 post request method
# ### we pass the arguments of form 
# #payload={'key1':'value1','key2':'value2'}
# #r=requests.post('http://httpbin.org/post',data=payload)
# #print r.text
# 
# ##here add the json Format data
# #url='http://httpbin.org/post'
# #payload={'some':'data'}
# #r=requests.post(url,data=json.dumps(payload))
# #print r.text
# 
# 
# ###here I will upload teh file to the website
# #url='http://httpbin.org/post'
# #files={'file':open(r'G:\MyCode\Python\spyderLearning\test.txt','rb')}
# #r=requests.post(url,files=files)
# #print r.text
# 
# ##if your file is large, you can use the stream.
# #with open('massive-body') as f:
# #    requests.post('http://some.url/streamed', data=f)
#==============================================================================

#==============================================================================
# ###3 Cookies
# url='http://exmple.com'
# r=requests.get(url)
# print r.cookies
# print r.cookies['key']
#==============================================================================

#==============================================================================
# #4 timeout settings
# requests.get('http://github.com',timeout=0.001)
#==============================================================================

#==============================================================================
# #5 Session 会话对象
# #r1=requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# #print r1.text
# #r2=requests.get('http://httpbin.org/cookies')
# #print r2.text
# 
# ###the solution to establish a session
# #s=requests.session()
# ##set the session
# #s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# ##get the session 
# #r=s.get('http://httpbin.org/cookies')
# #print r.text
# 
# ###update the session (as the session is a global variable)
# #1 s.headers.update and s.get is the TWO methods to update the session
# # 2 set the None to disable the global variable.
# s=requests.Session()
# s.headers.update({'x-test':'true'})
# r=s.get('http://httpbin.org/headers',headers={'x-test2':'true','x-customer':'1000'})
# print r.text
# 
# r=s.get('http://httpbin.org/headers',headers={'x-test':None})
# print r.text
#==============================================================================

#==============================================================================
# # 6 get the SSL vertificate file [https website]
# #r=requests.get("https://kyfw.12306.cn/otn/",verify=True)
# r=requests.get("https://kyfw.12306.cn/otn/",verify=False)
# print r.text
# 
# #re=requests.get("https://github.com",verify=True)
# #print r.text
#==============================================================================

#7 Proxy 代理
proxies={"https":"http://41.118.132.69:4433"}
r=requests.post("http://httpbin.org/post",proxies=proxies)
print r.text



