# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 14:23:14 2017

@author: sunnyday
"""

__author__ = 'CQC'
# -*- coding:utf-8 -*-

import urllib
import re

class Spider:

    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print( url)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return response.read().decode('gbk')

    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        for item in items:
            print (item[0],item[1],item[2],item[3],item[4])

spider = Spider()
spider.getContents(1)