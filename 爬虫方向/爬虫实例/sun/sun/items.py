# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SunItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    pushname = scrapy.Field()
    pushtime = scrapy.Field()
    content = scrapy.Field()
    content_img = scrapy.Field()
