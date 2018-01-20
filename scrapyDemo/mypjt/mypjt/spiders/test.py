# -*- coding: utf-8 -*-
import scrapy
from mypjt.items import MypjtItem

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['sina.com.cn']
    start_urls = ('http://news.sina.com.cn/c/2018-01-20/doc-ifyquixe4876505.shtml',
                  'http://sina.com.com')

    def parse(self, response):
        item  = MypjtItem()
        item['urlname'] = response.xpath('/html/head/title/text()')
        item['key'] = response.xpath('//meta[@name="keywords"]/@content').extract()
        yield item
