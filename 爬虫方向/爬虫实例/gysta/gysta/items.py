# -*- coding: utf-8 -*-
import scrapy

class GystaItem(scrapy.Item):
    TOURNAME = scrapy.Field()
    TOURTYPE = scrapy.Field()
    TOURTYPE1 = scrapy.Field()
    TOURNUM = scrapy.Field()
    ORIGIN = scrapy.Field()
    TOURLINE = scrapy.Field()
    HOTEL = scrapy.Field()
    STARTDATE = scrapy.Field()
    ENDDATE = scrapy.Field()
    AMOUNT = scrapy.Field()
    STATUS = scrapy.Field()

