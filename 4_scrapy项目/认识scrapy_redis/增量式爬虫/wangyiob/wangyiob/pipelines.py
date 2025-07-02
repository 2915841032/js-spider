# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo


class WangyiobPipeline:
    def open_spider(self, spider):
        if spider.name == "wangyi":
            self.mongo_client = pymongo.MongoClient('mongodb://root:root@localhost:27017/')
            self.collection = self.mongo_client['py_spider']['wangyijob']

    def process_item(self, item, spider):
        if spider.name == "wangyi":
            type_ = item.get('type')
            if type_ == 'info':
                self.collection.insert_one(item)
                print('插入成功:', item.get('id'))
            else:
                print('类型不符合规定...')
        return item

    def close_spider(self, spider):
        if spider.name == "wangyi":
            self.mongo_client.close()
