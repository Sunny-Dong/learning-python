    # -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 15:56:26 2017

@author: sunnyday
"""
from bs4 import BeautifulSoup
#Beautiful Soup，有了它我们可以很方便地提取出HTML或XML标签中的内容
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup=BeautifulSoup(html)
soup1=BeautifulSoup(open('hello.html'))
print(soup.prettify())
print(soup.title)
print(soup.head)
print(soup.a)
print(type(soup.a))

print soup.name
print soup.head.name
#[document]
#head
print soup.p['class']
#['title']

#对属性内容进行修改
soup.p['class']="newClass"
print soup.p
#<p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>

#删除
del soup.p['class']
print soup.p
#<p name="dromouse"><b>The Dormouse's story</b></p>

##获得标签内部文字 
'''.string'''
print soup.p.string
#The Dormouse's story