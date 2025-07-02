# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WangyijobPipeline:
    def open_spider(self, spider):
        self.mongo_client = pymongo.MongoClient('mongodb://root:root@localhost:27017/')
        self.collection = self.mongo_client['py_spider']['netEase_job']

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        print('保存成功:', item)
        return item

    def close_spider(self, spider):
        self.mongo_client.close()
