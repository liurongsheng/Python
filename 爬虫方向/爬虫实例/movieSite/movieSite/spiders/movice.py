# -*- coding: utf-8 -*-
import scrapy
from movieSite.items import MoviesiteItem

class MoviceSpider(scrapy.Spider):
    name = 'movice'
    allowed_domains = ['www.lalalo.com']
    start_urls = ['http://www.lalalo.com/type/1.html']

    def parse(self, response):
        movieItems = response.xpath("//div[@class='movie-item']")
        for movieItem in movieItems:
            item = MoviesiteItem()
            item['movieTitle'] = movieItem.xpath("./a/@title").get()
            item['movieImgUrl'] = movieItem.xpath("./a/img/@src").get()
            item['movieStatus'] = movieItem.xpath("./a/button/text()").get()
            item['pushTime'] = movieItem.xpath("./div[@class='meta']//span/text()").get()
            item['movieDetailUrl'] = movieItem.xpath("./a/@href").get()
            item['movieDetailUrl'] = 'http://www.lalalo.com' + item['movieDetailUrl']
            yield scrapy.Request(
                item['movieDetailUrl'],
                callback=self.movieDetailUrl,
                meta={"item": item}
            )
        next_url = response.xpath("//a[text()='下一页']/@href").get()
        next_url = 'http://www.lalalo.com' + next_url
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def movieDetailUrl(self, response):
        item = response.meta["item"]
        item['movieDetailDirect'] = response.xpath("//tbody//tr[1]//td[2]/text()").get()
        item['movieDetailActors'] = response.xpath("//tbody//tr[2]//td[2]/text()").get()
        item['movieDetailType'] = response.xpath("//tbody//tr[3]//td[2]/text()").get()
        item['movieDetailRelease'] = response.xpath("//tbody//tr[4]//td[2]/text()").get()
        item['movieDetailCountry'] = response.xpath("//tbody//tr[5]//td[2]/text()").get()
        item['movieDetailLanguage'] = response.xpath("//tbody//tr[6]//td[2]/text()").get()
        item['movieDetailGrade'] = response.xpath("//tbody//tr[7]//td[2]/text()").get()
        item['movieDetailStory'] = response.xpath("//tbody//tr[8]//td[2]/text()").get()
        print(item)
        yield item
