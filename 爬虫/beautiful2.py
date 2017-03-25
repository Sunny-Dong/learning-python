# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:11:17 2017

@author: sunnyday
"""

'''tag 的 .content 属性可以将tag的子节点以列表的方式输出'''
print( soup.head.contents )
#[<title>The Dormouse's story</title>]
print( soup.head.contents [0]) #列表索引

'''.descendants 属性可以对所有tag的子孙节点进行递归循环     '''
for child in soup.descendants:
    print (child)
    
'''如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。
如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容'''
print soup.head.string
#The Dormouse's story
print soup.title.string
#The Dormouse's story   