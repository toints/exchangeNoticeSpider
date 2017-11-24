# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NoticespiderItem(scrapy.Item):
    # define the fields for your item here like:
    urlmd5 = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
