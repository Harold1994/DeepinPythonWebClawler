from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
import random
from scrapyDemo.myfirstpjt.myfirstpjt.settings import UAPOOL

class Uamid(UserAgentMiddleware):
    def __init__(self,ua=''):
        self.ua = ua
    def process_request(self, request, spider):
        thisua = random.choice(UAPOOL)
        print('当前使用的代理为： '+thisua)
        request.headers.setdefault("User-Agent",thisua)
