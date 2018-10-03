import scrapy
import re
from smzdm.items import SmzdmItem

class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['www.smzdm.com']
    # base_url = 'http://www.smzdm.com'
    start_urls = ['https://www.smzdm.com/p1/']
    searchName = '当当优品'
    def parse(self, response):
        mainLlist = response.xpath("//ul[@class='feed-list-hits']//li")
        for list in mainLlist:
            title = list.xpath(".//h5/a/text()").get()
            href = list.xpath(".//h5/a/@href").get()
            referrerName = list.xpath(".//div[@class='feed-block-info']//span/text()").get()
            starNum = list.xpath(".//div[@class='z-feed-foot-l']//a[1]//span[@class='unvoted-wrap']/span/text()").get()
            againStarNum = list.xpath(".//div[@class='z-feed-foot-l']//a[2]//span[@class='unvoted-wrap']/span/text()").get()
            pushTime = list.xpath(".//div[@class='z-feed-foot-r']//span/text()").getall()
            pushTime = "".join(pushTime).strip()
            fromWhere = list.xpath(".//div[@class='z-feed-foot-r']//span/a/text()").get()
            res = re.search(self.searchName,title)
            if res == None:
                print(title)
            else:
                print('获取到一条数据：'+title)
                item = SmzdmItem(title=title,href=href,referrerName=referrerName,starNum=starNum,
                                 againStarNum=againStarNum,pushTime=pushTime,fromWhere=fromWhere,)
                yield item

        next_url = response.xpath("//div[@class='feed-pagenation']//ul//li[last()]//a/@href").get()
        print('*'*100)
        if not next_url:
            yield scrapy.Request('https://www.smzdm.com/p2/', callback=self.parse)
        else:
            yield scrapy.Request(next_url,callback=self.parse)