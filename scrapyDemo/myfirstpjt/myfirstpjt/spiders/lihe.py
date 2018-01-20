# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem


class LiheSpider(scrapy.Spider):
    name = 'lihe'
    # allowed_domains = ['sina.com.cn']

    start_urls = ('http://news.sina.com.cn/c/2018-01-20/doc-ifyquixe4876505.shtml',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_205_60177.html#p=1',
                  'http://ent.sina.com.cn/s/h/2018-01-20/doc-ifyqtwzv0600740.shtml')
    # def __init__(self, myurl=None, *args, **kwargs):
    #     super(LiheSpider, self).__init__(*args, **kwargs)
    #     myurllist = myurl.split('|')
    #     for url in myurllist:
    #         print("要爬取的网址是: %s" % myurl)
    #     self.start_urls = myurllist

    # url2 =('http://sina.com.cn/',
    #        'http://jd.com.cn')

    # def start_requests(self):
    #     for url in self.url2:
    #         yield self.make_requests_from_url(url)
    # 带有 yield 的函数在 Python 中被称之为 generator（生成器）

    def parse(self, response):
        item = MyfirstpjtItem()
        item['urlname'] = response.xpath('/html/head/title/text()')
        print("以下将显示网址标题:")
        print(item['urlname'])


