# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from scrapy.pipelines.images import ImagesPipeline
from urllib.parse import urlparse
from scrapy.http import Request


class AutohomeImagesPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        for image_url in item['image_urls']:
            yield Request(image_url,meta={'title':item['title']})
    def file_path(self, request, response=None, info=None):
        path = 'images/' + ''.join(request.meta['title']) + '/' + os.path.basename(urlparse(request.url).path)
        return path


    