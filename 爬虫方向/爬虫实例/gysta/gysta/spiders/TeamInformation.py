# -*- coding: utf-8 -*-
import scrapy
import re
import math
from gysta.items import GystaItem
class TeaminformationSpider(scrapy.Spider):
    name = 'TeamInformation'
    allowed_domains = ['activity.gysta.gov.cn']
    # start_urls = ['http://activity.gysta.gov.cn/common_execute.action?path=teams']
    pageNo = '1'
    pageSize = '60'

    def start_requests(self):
        yield scrapy.FormRequest(
            url='http://activity.gysta.gov.cn/common_execute.action',
            formdata={
                'path': 'teams',
                'name': '请输入关键字查询',
                'pageNo': self.pageNo,
                'pageSize': self.pageSize,
                'orderBy': '',
                'orderType': ''
            },
        callback = self.parse
        )
    def parse(self, response):
        total_tr = response.xpath("//div[@id='infos']/span/text()").get()
        total_tr = int(re.findall('\d+', total_tr)[0])
        pageSize = int(self.pageSize)
        total_pageNum = math.ceil(total_tr / pageSize)
        tr_list = response.xpath("//table[@class='tableTeam']//tr")[1:]
        for tr in tr_list:
            item = GystaItem()
            item["TOURNAME"] = tr.xpath(".//td[1]//a/text()").get()
            item["TOURTYPE"] = tr.xpath(".//td[2]//text()").get()
            item["TOURTYPE1"] = tr.xpath(".//td[3]//text()").get()
            item["TOURNUM"] = tr.xpath(".//td[4]//text()").get()
            item["ORIGIN"] = tr.xpath('normalize-space(.//td[5]//text())').get()
            item["TOURLINE"] = tr.xpath(".//td[6]//text()").get()
            item["HOTEL"] = tr.xpath('normalize-space(.//td[7]//text())').get()
            item["STARTDATE"] = tr.xpath('normalize-space(.//td[8]//text())').get()
            item["ENDDATE"] = tr.xpath('normalize-space(.//td[9]//text())').get()
            item["AMOUNT"] = tr.xpath('normalize-space(.//td[10]//text())').get()
            item["STATUS"] = tr.xpath('normalize-space(.//td[11]//text())').get()
            print(item)
            yield item
        if total_pageNum > int(self.pageNo) :
            self.pageNo = str( int(self.pageNo) +1)
            yield scrapy.FormRequest(
                url='http://activity.gysta.gov.cn/common_execute.action',
                formdata={
                    'path': 'teams',
                    'name': '请输入关键字查询',
                    'pageNo': self.pageNo,
                    'pageSize': self.pageSize,
                    'orderBy': '',
                    'orderType': ''
                },
                callback=self.parse
            )
