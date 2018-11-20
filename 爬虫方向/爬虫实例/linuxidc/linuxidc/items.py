import scrapy


class LinuxidcItem(scrapy.Item):
    bookName = scrapy.Field()
    bookPushTime = scrapy.Field()
    downloadUrl = scrapy.Field()
