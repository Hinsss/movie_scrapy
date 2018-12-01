# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoublekillItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义数据结构
    face = scrapy.Field()
    name = scrapy.Field()
    age = scrapy.Field()
    content = scrapy.Field()
    haha_count = scrapy.Field()
    ping_count = scrapy.Field()
