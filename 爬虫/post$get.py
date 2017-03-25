# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:32:25 2017

@author: sunnyday

"""
'''POST'''
import urllib

values = {"username":"1016903103@qq.com","password":"XXXX"}
values=urllib.parse.urlencode(values)
data=values.encode(encoding='UTF8')
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url,data)   ##设置参数
response = urllib.request.urlopen(request)
print (response.read())

'''GET
至于GET方式我们可以直接把参数写到网址上面，直接构建一个带参数的URL出来即可'''
import urllib
values = {"username":"1016903103@qq.com","password":"XXXX"}
values=urllib.parse.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+values
print(geturl)
request = urllib.request.Request(geturl)
response = urllib.request.urlopen(request)
print (response.read())
