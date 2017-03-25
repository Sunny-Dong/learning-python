# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:15:59 2017

@author: sunnyday
"""

'''搜索文档树  标签
find_all( name , attrs , recursive , text , **kwargs )
find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉'''
print(soup.find_all('a'))

'''如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.
下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到'''
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b

'''如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.
下面代码找到文档中所有<a>标签和<b>标签'''
soup.find_all(["a", "b"])

'''True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点'''
for tag in soup.find_all(True):
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a

soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]

'''在这里我们想用 class 过滤，不过 class 是 python 的关键词，
这怎么办？加个下划线就可以'''
soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

'''通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样,
 text 参数接受 字符串 , 正则表达式 , 列表, True'''
 soup.find_all(text="Elsie")
# [u'Elsie']

soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']

soup.find_all(text=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]


soup.find_all(text="Elsie")
# [u'Elsie']

soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']

soup.find_all(text=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]
 
'''.类名 #id a[class="sister"'''
printsoup.select('p #link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
 
 
 
 