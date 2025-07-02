# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import redis
import hashlib
import pymongo
from scrapy.exceptions import DropItem
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TxWorkCheckPipeline:
    def open_spider(self, spider):
        if spider.name == 'tx_work_info':
            self.redis_client = redis.Redis()

    def process_item(self, item, spider):
        if spider.name == 'tx_work_info':
            item_str_data = json.dumps(item)
            md5_hash = hashlib.md5()
            md5_hash.update(item_str_data.encode())  # mac/linux默认编码是utf-8
            hash_value = md5_hash.hexdigest()
            if self.redis_client.get(f'tx_work_item_filter: {hash_value}'):
                raise DropItem('数据重复...')
            else:
                self.redis_client.set(f'tx_work_item_filter: {hash_value}', item_str_data)
            return item

    def close_spider(self, spider):
        if spider.name == 'tx_work_info':
            self.redis_client.close()


class TxWorkFilePipeline:
    def open_spider(self, spider):
        # 爬虫开启时仅运行一次
        if spider.name == 'tx_work_info':
            self.file_obj = open('tx_json_data.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == 'tx_work_info':
            print('TxWorkFilePipeline被执行...')
            self.file_obj.write(json.dumps(item, ensure_ascii=False, indent=4) + '\n')
            return item  # 将数据写入完成之后把原数据传递给下一个pipeline

    def close_spider(self, spider):
        # 爬虫关闭时仅运行一次
        if spider.name == 'tx_work_info':
            self.file_obj.close()


class TxWorkMongoPipeline:
    def open_spider(self, spider):
        # 爬虫开启时仅运行一次
        if spider.name == 'tx_work_info':
            print('open_spider被执行...')
            self.mongo_client = pymongo.MongoClient()
            self.collection = self.mongo_client['py_spider']['scrapy_tx_work']

    def process_item(self, item, spider):
        if spider.name == 'tx_work_info':
            print('TxWorkMongoPipeline被执行...')
            self.collection.insert_one(item)
            print('数据插入成功:', item)

    def close_spider(self, spider):
        # 爬虫关闭时仅运行一次
        if spider.name == 'tx_work_info':
            print('close_spider被执行...')
            self.mongo_client.close()
