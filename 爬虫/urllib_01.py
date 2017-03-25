# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:32:07 2017

@author: sunnyday
"""

'''用户输入网址之后，经过DNS服务器，找到服务器主机，
向服务器发出一个请求，服务器经过解析之后，
发送给用户的浏览器 HTML、JS、CSS 等文件，
浏览器解析出来，用户便可以看到形形色色的图片了。'''

'''用户看到的网页实质是由 HTML 代码构成的，爬虫爬来的便是这些内容，
通过分析和过滤这些 HTML 代码，实现对图片、文字等资源的获取。'''
'''爬虫爬取数据时必须要有一个目标的URL才可以获取数据，'''

import urllib.request
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)


'''GET方式是直接以链接形式访问，链接中包含了所有的参数
POST则不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便了'''

'''要抓取百度上面搜索关键词为Jecvay Notes的网页'''
import urllib
import urllib.request
data={}
data['word']='Jecvay Notes'
url_values=url.parse.urlencode(data) #把一个通俗的字符串, 转化为url格式的字符串
url="http://www.baidu.com/s?"
full_uri=url+url_values
data=urllib.request.urlopen(full_url).read()
print(data)

