# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mycwpjt.items import MycwpjtItem


class LiheSpider(CrawlSpider):
    name = 'lihe'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/n.*?shtml')), callback='parse_item', follow=True),)

    def parse_item(self, response):
        i = MycwpjtItem()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        i['name'] = response.xpath('/html/head/title/text()').extract()
        i['link'] = response.xpath('//link[@rel="canonical"]/@href').extract()
        return i
