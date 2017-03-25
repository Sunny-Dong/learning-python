# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanNewMovieItem(scrapy.Item):   ##这个是用来储存要爬下来的数据的存放容器
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name=scrapy.Field()
    movie_star=scrapy.Field()
    movie_url=scrapy.Field()

