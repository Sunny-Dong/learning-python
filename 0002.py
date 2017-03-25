# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:37:29 2017

@author: sunnyday
"""
#sqlite
import sqlite3
def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value='0'
    return float(value)
    
conn=sqlite3.connect('food.db')
curs=conn.cursor() ##游标 用来执行sql查询

curs.execute('''
CREATE TABLE protein02(
 id      text primarykey,
 desc    text,
 water   float,
 kcal    float,
 protein float,
 fat     float,
 ash     float,
 carbs   float,
 fiber   float,
 suger   float
 )
''')
query='INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
field_count=10
for line in open('ABBREV.txt'):
    fields=line.split('^')
    vals=[convert(f) for f in fields[:field_count]]
    curs.execute(query,vals)
    
    
    
conn.commit() ##提交
conn.close()  ##关闭

