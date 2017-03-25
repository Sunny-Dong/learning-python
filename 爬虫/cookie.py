# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 10:34:06 2017

@author: sunnyday
"""

import urllib
import http.cookiejar
#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
#声明一个CookieJar对象实例来保存cookie
#cookie = http.cookiejar.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)  
response = opener.open('http://www.baidu.com')
for item in cookie:
    print ('Name = '+item.name)
    print ('Value = '+item.value)
    
    
'''文件中读取cookie'''
#创建MozillaCookieJar实例对象
cookie = http.cookiejar.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = urllib.request.Request("http://www.baidu.com")
handler=urllib.request.HTTPCookieProcessor(cookie)
#利用urllib2的build_opener方法创建一个opener
opener = urllib.request.build_opener(handler)
response = opener.open(req)
print (response.read())


'''利用cookie模拟网站登录'''
import urllib
import http.cookiejar

filename = 'xuanke.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie =http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
postdata = urllib.parse.urlencode({
			'stuid':'dongxinyu',
			'pwd':'kobe2481023dxy'
		})
postdata=postdata.encode(encoding='UTF8')
#登录教务系统的URL
loginUrl = 'https://jaccount.sjtu.edu.cn/jaccount/jalogin?sid=jagraduate20130107&returl=%43%4f%71%6c%4c%5a%50%45%58%31%50%64%48%76%53%74%32%45%37%77%78%67%57%56%73%67%4a%46%34%6e%4e%37%52%55%35%72%33%43%30%70%59%36%4d%6a%57%64%45%4e%6f%46%71%39%65%65%4e%48%34%67%75%4f%44%78%4b%68%73%64%73%79%4a%50%74%4e%59%43%4b%33%4b%68%37%4e%6d%4e%6d%64%6a%4c%4e%6d%32%41%6b%6f%52%65%76%4c%47%74%61%67%5a%6b%64%32%2b%73%56%30&se=%43%46%52%64%6c%6d%6e%46%41%72%35%67%57%6b%70%4d%64%6c%73%4a%54%33%4f%49%38%57%4e%35%36%61%46%63%36%41%31%52%69%77%6a%46%51%4b%48%35'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://www.yjs.sjtu.edu.cn/ssfw/index.do'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print (result.read())