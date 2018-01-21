# -*- coding: utf-8 -*-
import urllib.request

import scrapy
from scrapy.http import Request, FormRequest


class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    allowed_domains = ['douban.com']
    header = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0"}

    def start_requests(self):
        return [Request('https://accounts.douban.com/login', meta={"cookiejar": 1},
                        callback=self.parse,headers=self.header)]

    def parse(self, response):
        print("------------------------")
        captcha = response.xpath("//img[@id='captcha——i']/@src").extract()
        if len(captcha) > 0:
            print("有验证码")
            localpath = "/media/harold/SpareDisk/pythonProject/pic/chaptcha.png"
            urllib.request.urlretrieve(captcha[0], localpath)
            print('请通过本地查看验证照片输入验证码:')
            captchavalue = input()
            data = {
                'form_email': '18911341910',
                "form_password": 'lh1994114',
                'captcha-solution': captchavalue,
                'redir': 'https://www.douban.com/people/172915333/'
            }
        else:
            print("无验证码")
            data = {
                'form_email': '18911341910',
                "form_password": 'lh1994114',
                'redir': 'https://www.douban.com/people/172915333/'
            }

        print("登录中...")

        return [FormRequest.from_response(response, meta={'cookiejar': response.meta['cookiejar']},headers=self.header,formdata=data,
                                          callback=self.next,)]

    def next(self, response):
        print('此时已经完成登录')
        xtitle = '/html/head/title/text()'
        # xnotetitle = '//div[@class="note-header pl2"]/a/@title'
        # xnotetime = '//div[@class="note-header pl2"]//span[@class="pl"]/text()'
        # xnotecontent = "//div[@class='mbtr2']/div[@class='note']/text()"
        # xnoteurl = "//div[@class='note-header pl2']/a/@href"
        title = response.xpath(xtitle).extract()
        # notetitle = response.xpath(xnotetitle).extract()
        # notetime = response.xpath(xnotetime).extract()
        # notecontent = response.xpath(xnotecontent).extract()
        # noteurl = response.xpath(xnoteurl).extract()
        print("title:" + title)
        # for i in range(0,len(notetitle)):
        #     print("文章" + str(i+1))
        #     print('notetitle: '+notetitle)
        #     print('notetime: '+ notetime)
        #     print('notecontent: ' + notecontent)
        #     print('noteurl: ' + noteurl)

