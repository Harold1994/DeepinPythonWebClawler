# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

class QtpjtPipeline(object):

    def process_item(self, item, spider):
        for i in range(0,len(item['picurl'])):
            thispic = item['picurl'][i]
            trueurl = thispic+"_1024.jpg"
            local_path ="/media/harold/SpareDisk/pythonProject/pic/" + str(i) + ".jpg"
            urllib.request.urlretrieve(trueurl,filename=local_path)
        return item
