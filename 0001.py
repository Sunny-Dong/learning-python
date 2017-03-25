# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:21:06 2017

@author: sunnyday
"""

#第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）

import random, string
#ascii_letters是生成所有字母 从a-z和A-Z digits是生成所有数字0-9.
forSelect = string.ascii_letters + string.digits
#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
##count=200,lengh=20
def sequence(count,lengh):
    for i in range(count):
        seq=''
        for j in range(lengh):
            seq+=random.choice(forSelect)  
        print(seq)
if __name__=='__main__':
    sequence(200,10)
 