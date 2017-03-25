# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:37:36 2017

@author: sunnyday
"""
import re
import requests
story=[]
url='http://www.jianshu.com/p/62e0a588ee0d'
response=requests.get(url).text  
pattern=re.compile('<pre><code>(.*?)</code></pre>',re.S,)      
items=re.findall(pattern,response)   
print (items)