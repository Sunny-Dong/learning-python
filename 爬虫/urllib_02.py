# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:30:30 2017

@author: sunnyday
"""
##队列
from collections import deque
queue = deque(["Eric", "John", "Michael"])  ## deque(['Eric', 'John', 'Michael'])
queue.append("Terry")           # Terry 入队
queue.append("Graham")          # Graham 入队
queue.popleft()                 # 队首元素出队
#输出: 'Eric'
queue.popleft()                 # 队首元素出队
#输出: 'John'
queue                           # 队列中剩下的元素
#输出: deque(['Michael', 'Terry', 'Graham'])


##集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                    # 这里演示的是去重功能
'''{'orange', 'banana', 'pear', 'apple'}'''
a = set('abracadabra')
b = set('alacazam')
a    #{'a', 'r', 'b', 'c', 'd'}
a-b
a|b  #a或b
a&b  #a且b
a^b  #ab对称差 不同时包含于a和b


''' 爬回来的数据是一个字符串, 字符串的内容是页面的html代码. 
我们要从字符串中, 提取出页面提到过的所有url. '''


import re
import urllib.request
import urllib
 
from collections import deque
 
queue = deque()
visited = set()
 
url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的
 
queue.append(url)
cnt = 0
 
while queue:
  url = queue.popleft()  # 队首元素出队
  visited |= {url}  # 标记为已访问
 
  print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
  cnt += 1
  urlop = urllib.request.urlopen(url)
  if 'html' not in urlop.getheader('Content-Type'):
    continue
 
  # 避免程序异常中止, 用try..catch处理异常
  try:
    data = urlop.read().decode('utf-8')
  except:
    continue
 
  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  linkre = re.compile('href=\"(.+?)\"')
  for x in linkre.findall(data):
    if 'http' in x and x not in visited:
      queue.append(x)
      print('加入队列 --->  ' + x)