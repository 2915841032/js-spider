# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 分两个pipeline写入图片和数据
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import pymongo
import os


class DoubanPipeline:
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        # 设置MongoDB连接
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def process_item(self, item, spider):
        del item['img']
        # 对字段进行处理
        self.collection.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


class DoubanImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 这个方法需要被覆盖以防止默认行为
        pass

    def file_path(self, request, response=None, info=None, *, item=None):
        # 这个方法需要被覆盖以防止默认行为
        pass

    def process_item(self, item, spider):
        # 将数据写入MongoDB
        self.download_dir = os.path.join(os.getcwd(), 'downloads')
        os.makedirs(self.download_dir, exist_ok=True)

        image_path = os.path.join(self.download_dir, item['title'])

        with open(image_path + '.jpg', 'wb') as f:
            f.write(item['img'])
        return item


