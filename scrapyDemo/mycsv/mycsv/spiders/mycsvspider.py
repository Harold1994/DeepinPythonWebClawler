# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem
import scrapy.commands.crawl

class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers = ['name', 'sex', 'addr', 'email']
    delimiter = ','

    # Do any adaptations you need here
    # def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        # i['url'] = row['url']
        # i['name'] = row['name']
        # i['description'] = row['description']
        i['name'] = row['name'].encode()

        i['sex'] = row['sex'].encode()
        print("name:", i['name'])
        print("sex", i['sex'])
        print("--------------------")
        return i
