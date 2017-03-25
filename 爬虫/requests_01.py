# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 15:32:00 2017

@author: sunnyday
"""
import requests

r = requests.get('http://cuiqingcai.com')
print (type(r))
soup=BeautifulSoup("""r""")
print (r.status_code)
print (r.encoding)
#print r.text
print (r.cookies)
#打印出了返回结果的类型，状态码，编码方式，Cookies
'''<class 'requests.models.Response'>
200
UTF-8
<RequestsCookieJar[]>'''

#包含了http的所有请求方式                 
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")                  

##get添加参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)



url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print (r.text)

'''超时配置'''
requests.get('http://github.com', timeout=0.001)

##SSL
r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
print (r.text)


