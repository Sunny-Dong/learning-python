# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:30:35 2017

@author: sunnyday
"""
from lxml import etree
import re
import urllib
import requests
from bs4 import BeautifulSoup
url='https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'
html=requests.get(url).text
#soup=BeautifulSoup(html)
#print(soup.title)
#<title>纯原创我心中的NBA2014-2015赛季现役50大_nba吧_百度贴吧</title>
html = etree.HTML(html)
result = etree.tostring(html)
print(result)
result1=html.xpath('//div/@class');print(result1)
result = html.xpath('//li//span')
print (result)

pattern = re.compile('<title>(.*?)</title>',re.S)
result=re.search(pattern,html)
print(result.group(1))

pattern = re.compile('<div class="p_content.*?>.*?<img.*?>(.*?)</div>',re.S)
result=re.search(pattern,html)
print(result.group(1))
def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<title>(.*?)</title>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1)  #测试输出
            return result.group(1).strip()
        else:
            return None

#获取帖子一共有多少页
print(soup.li)
print(soup.prettify())  
print(soup.div)
print(soup.a.contents)       
print(soup.br)        
           
        
        
        
        
        