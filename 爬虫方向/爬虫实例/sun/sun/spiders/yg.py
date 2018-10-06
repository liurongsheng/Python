# -*- coding: utf-8 -*-
import scrapy
from sun.items import SunItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/html/top/report.shtml']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='greyframe']/table[2]//table//tr")
        for tr in tr_list:
            item = SunItem()
            item["title"] = tr.xpath("./td[2]/a[@class='news14']/@title").extract_first()
            item["href"] = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item["pushname"] = tr.xpath("./td[4]/text()").extract_first()
            item["pushtime"] = tr.xpath("./td[last()]/text()").extract_first()

            yield scrapy.Request(
                item['href'],
                callback = self.parse_detail,
                meta = {"item":item}
            )
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback = self.parse
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='c1 text14_2']/text()").extract()
        item["content_img"] = response.xpath("//div[@class='c1 text14_2']//img/@src").extract()
        item["content_img"] = ["http://wz.sun0769.com"+i for i in item["content_img"]]
        yield item
