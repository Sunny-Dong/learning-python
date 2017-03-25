# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:29:26 2017

@author: sunnyday
"""
##http://liam0205.me/2015/05/05/pil-tutorial-imagedraw-and-imagefont/
'''PIL简明教程'''
__author__ = 'sunny'

from PIL import Image,ImageDraw,ImageFont
import random

msgNum = str(random.randint(1,99)) ##随机数

# Read image
im = Image.open('1.jpg')
w,h = im.size
wDraw = 0.8 * w
hDraw = 0.08 * w
# Draw image
'''Draw 类提供了 text(position, string, options) 方法，
该方法可以在 Image 实例上写字'''

font = ImageFont.truetype('C:/Users/sunnyday/Anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Bold.ttf', 50) # use absolute font path to fix 'IOError: cannot open resource'
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw),msgNum,fill=(255,83,0),font=font)

#text(position, string, options)
# Save image
im.save('manu.jpg')