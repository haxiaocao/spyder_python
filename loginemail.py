# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# reference site：http://cuiqingcai.com/947.html

import urllib2
import urllib
import json


values={}
values['email']='guokai2007'
values['password']='lovegodgood101'  
#values['auto-id-1497686306151']='guokai2007'
#values['auto-id-1497686306154']='lovegodgood101' 
data=urllib.urlencode(values)
print data
url=r'http://mail.163.com/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36' 
headers = { 'User-Agent' : user_agent,
             #'Referer':'http://mail.163.com/' ,
             'accept': '*/*'}  
request = urllib2.Request(url,data,headers=headers)
request.get_method = lambda : 'HEAD'
print request.data
try:
    response=urllib2.urlopen(request)
    msg=response.read()
    response.close()
    #print response.code
    print "Here are the result:"
    print msg
    print len(msg)
    
except Exception ,ex:
    print ex.code  # 405, header should add some other stuff.
    print ex.reason





























