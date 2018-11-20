# -*- coding: utf-8 -*-
import scrapy
from linuxidc.items import LinuxidcItem

class LinuxftpSpider(scrapy.Spider):
    name = 'linuxFtp'
    allowed_domains = ['linux.linuxidc.com']
    start_urls = ['https://linux.linuxidc.com/index.php']
    base_url = 'https://linux.linuxidc.com/'

    def parse(self, response):
        trs = response.xpath("//tr[@class ='folder_bg']")
        for tr in trs:
            if tr is not "2011年资料" and tr is not "pub":
                item = LinuxidcItem()
                trHref = tr.xpath(".//a/@href").get()
                yearDetailUrl = self.base_url + trHref
                yield scrapy.Request(
                    yearDetailUrl,
                    callback=self.yearDetail,
                    meta={"item": item}
                )

    def yearDetail(self, response):
        item = response.meta["item"]
        mouthDetailTrs = response.xpath("//tr[@class ='folder_bg']")
        for mouthDetailTr in mouthDetailTrs:
            mouthDetailUrl = mouthDetailTr.xpath(".//a/@href").get()
            mouthDetailUrl = self.base_url + mouthDetailUrl
            yield scrapy.Request(
                mouthDetailUrl,
                callback=self.mouthDetail,
                meta={"item": item}
            )

    def mouthDetail(self, response):
        item = response.meta["item"]
        dayDetailTrs = response.xpath("//tr[@class ='folder_bg']")
        for dayDetailTr in dayDetailTrs:
            dayDetailUrl = dayDetailTr.xpath(".//a/@href").get()
            dayDetailUrl = self.base_url + dayDetailUrl
            yield scrapy.Request(
                dayDetailUrl,
                callback=self.dayDetail,
                meta={"item": item}
            )

    def dayDetail(self, response):
        item = response.meta["item"]
        dayDetailTrs = response.xpath("//tr[@class ='folder_bg']")
        for dayDetailTr in dayDetailTrs:
            detailUrl = dayDetailTr.xpath(".//a/@href").get()
            detailUrl = self.base_url + detailUrl
            print(detailUrl)
            yield scrapy.Request(
                detailUrl,
                callback=self.detail,
                meta={"item": item}
            )

    def detail(self, response):
        item = response.meta["item"]
        detailTrs = response.xpath("//tr[@class ='file_bg1']")
        for detailTr in detailTrs:
            item['bookName'] = detailTr.xpath(".//a/text()").get()
            downloadUrl = detailTr.xpath(".//a/@href").get()
            item['downloadUrl'] = self.base_url + downloadUrl
            item['bookPushTime'] = detailTr.xpath(".//td[last()]/text()").get()
            print(item)
            yield item