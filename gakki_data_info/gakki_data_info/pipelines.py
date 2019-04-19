# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class GakkiDataInfoPipeline(object):

    def process_item(self, item, spider):
        client = MongoClient()
        ret = {'用户名': item['name'], '排名': item['rank'], '经验值': item['exp'], '等级': item['level']}
        collection = client['新垣结衣吧发帖情况']['用户信息'].insert(ret)
        print(1111)
        return item
