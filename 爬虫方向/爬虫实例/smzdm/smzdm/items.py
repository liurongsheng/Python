# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SmzdmItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    referrerName = scrapy.Field()
    starNum = scrapy.Field()
    againStarNum = scrapy.Field()
    pushTime = scrapy.Field()
    fromWhere = scrapy.Field()
