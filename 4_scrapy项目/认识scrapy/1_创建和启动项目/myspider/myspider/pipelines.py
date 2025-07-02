# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

# useful for handling different item types with a single interface

import pymongo
from scrapy.exceptions import NotConfigured

# 导入scrapy的设置


import os
import pymongo
from scrapy.exceptions import NotConfigured


class QingtingPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        mongo_uri = crawler.settings.get('MONGO_URI')
        mongo_db = crawler.settings.get('MONGO_DATABASE', 'qingting')

        if not mongo_uri:
            raise NotConfigured("MongoDB URI is missing")

        return cls(mongo_uri, mongo_db)
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

        # 创建下载目录
        self.download_dir = os.path.join(os.getcwd(), 'downloads')
        os.makedirs(self.download_dir, exist_ok=True)
    def close_spider(self, spider):
        self.client.close()
    def process_item(self, item, spider):
        item_type = item.get('type')

        if item_type == 'info':
            self.process_info_item(item, spider)
        elif item_type == 'image':
            self.process_image_item(item)
        else:
            spider.logger.warning(f"Unknown item type: {item_type}")

        return item
    def process_info_item(self, item, spider):
        collection = self.db[spider.name]
        try:
            collection.insert_one(dict(item))
            spider.logger.info(f"Inserted info item: {item['title']}")
        except Exception as e:
            spider.logger.error(f"Failed to insert info item: {e}")
    def process_image_item(self, item):
        image_path = os.path.join(self.download_dir, item['image_name'])

        try:
            with open(image_path, 'wb') as f:
                f.write(item['image_content'])
            print(f"Successfully saved image: {item['image_name']}")
        except Exception as e:
            print(f"Failed to save image {item['image_name']}: {e}")
