# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # 数据库管道需求
    # define the fields for your item here like:
    # title = scrapy.Field()
    # type = scrapy.Field()
    # num = scrapy.Field()
    # position = scrapy.Field()
    # time = scrapy.Field()
    # 本地文件管道需求
    tou = scrapy.Field()
    content = scrapy.Field()
