# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from qtpjt.items import QtpjtItem
import re
class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/tb/']

    def parse(self, response):
        item = QtpjtItem()
        picurl = "(http://pic.qiantucdn.com/58pic/.*?).[jpeg|jpg]"
        item['picurl'] = re.compile(picurl).findall(str(response.body))
        item['picid'] = response.xpath('//a[@class="bottom-title"]/text()')
        yield item

        for i in range(1,20):
            nexturl = 'http://www.58pic.com/piccate/3-0-0-'+str(i)+'.html'
            yield Request(nexturl,callback=self.parse)

