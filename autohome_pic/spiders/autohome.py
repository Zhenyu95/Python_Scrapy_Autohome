# -*- coding: utf-8 -*-
import scrapy
from autohome_pic.items import ImageItem
import re


class AutohomeSpider(scrapy.Spider):
    name = 'autohome'
    start_urls = ['https://car.autohome.com.cn/pic/series/177.html']

    def parse(self, response):
        uiboxs = response.xpath('//div[@class="uibox"]')[1:]
        for each in uiboxs:
            title = each.xpath('.//div[@class="uibox-title"]/a[1]/text()').getall()
            imglinks = each.xpath('.//div[(@class="uibox-con carpic-list03") and not (@id="vrlist")]/ul/li/a/img/@src').getall()
            imglinks =list(map(lambda url:response.urljoin(url), imglinks))
            # for link in imglinks:
            #     link = re.sub(r'240x180.+autohomecar','1024x0_1_q95_autohomecar',link)
            imglinks =list(map(lambda link:re.sub(r'240x180.+autohomecar','autohomecar',link),imglinks))
            print('*'*400)
            print(imglinks)
            print('*'*400)
            item=ImageItem(title=title,image_urls=imglinks)
            yield item

        