# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesiteItem(scrapy.Item):
    movieTitle = scrapy.Field()
    movieImgUrl = scrapy.Field()
    movieStatus = scrapy.Field()
    pushTime = scrapy.Field()
    movieDetailUrl = scrapy.Field()
    movieDetailDirect = scrapy.Field()
    movieDetailActors = scrapy.Field() # 演员
    movieDetailType = scrapy.Field()
    movieDetailRelease = scrapy.Field() # 上映时间
    movieDetailCountry = scrapy.Field()
    movieDetailLanguage = scrapy.Field()
    movieDetailGrade = scrapy.Field()
    movieDetailStory = scrapy.Field()

