# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class HcInfoPipeline:
    def process_item(self, item, spider):
        return item


class MongoPipeline:
    def open_spider(self, spider):
        if spider.name == 'HcInfoData':
            self.mongo_client = pymongo.MongoClient('mongodb://root:root@localhost:27017')
            self.collection = self.mongo_client['py_spider']['scrapy_jc_info']

    def process_item(self, item, spider):
        if spider.name == 'HcInfoData':
            self.collection.insert_one(dict(item))  # 使用items文件校验后传递过来的item不是dict对象
            print('数据保存成功:', item)
            return item

    def close_spider(self, spider):
        if spider.name == 'HcInfoData':
            self.mongo_client.close()
