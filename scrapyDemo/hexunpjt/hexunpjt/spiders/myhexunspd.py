# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from hexunpjt.items import HexunpjtItem
from scrapy.http import Request


class MyhexunspdSpider(scrapy.Spider):
    name = 'myhexunspd'
    allowed_domains = ['hexun.com']
    uid = "whbsuwc"

    def start_requests(self):
        yield Request('http://msncnwy.blog.hexun.com/p1/default.html', headers={'User-Agent':
                                                                                                "Mozilla/5.0 ("
                                                                                                "Windows; U; "
                                                                                                "Windows NT 6.1; "
                                                                                                "en-US) "
                                                                                                "AppleWebKit/532.5 (KHTML, "
                                                                                                "like Gecko) "
                                                                                                "Chrome/4.0.249.0 "
                                                                                                "Safari/532.5 "})

    def parse(self, response):
        item = HexunpjtItem()
        item['name'] = response.xpath('//span[@class="ArticleTitleText"]/a/text()').extract()
        item['url'] = response.xpath('//span[@class="ArticleTitleText"]/a/@href').extract()
        pat1 = '<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)">'
        hcurl = re.compile(pat1).findall(str(response.body))[0]
        headers2 = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2 ')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers2]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(hcurl).read()

        pat2 = "click\d*?','(\d*?)'"
        pat3 = "comment\d*?','(\d*?)'"

        item['hits'] = re.compile(pat2).findall(str(data))
        item['comment'] = re.compile(pat3).findall(str(data))
        yield item
        pat4 = "blog.hexun.com/p(.*?)/"
        data2 = re.compile(pat4).findall(str(response.body))
        if (len(data) >= 2):
            totalurl = data2[-2]
        else:
            totalurl = 1
        # for i in range(2, int(totalurl) + 1):
        #     nexturl = "http://msncnwy.blog.hexun.com/p" + str(i) + "/default.html"
        #     yield Request(nexturl, callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
        #                                                                        'AppleWebKit/534.27 (KHTML, '
        #                                                                        'like Gecko) Chrome/12.0.712.0 '
        #                                                                        'Safari/534.27 '})
