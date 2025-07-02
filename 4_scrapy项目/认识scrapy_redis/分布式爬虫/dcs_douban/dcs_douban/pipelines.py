# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanPipeline:
    def open_spider(self, spider):
        if spider.name == "douban":
            self.mongo_client = pymongo.MongoClient('mongodb://root:root@localhost:27017/')
            self.collection = self.mongo_client['py_spider']['doubanTop250']

    def process_item(self, item, spider):
        if spider.name == "douban":
            type_ = item.get('type')
            if type_ == 'info':
                self.collection.insert_one(item)
                print('插入成功:', item.get('title'))
            elif type_ == 'douban':
                download_path = os.getcwd() + '/download/'
                if not os.path.exists(download_path):
                    os.mkdir(download_path)

                image_name = item.get('image_name')
                image_content = item.get('image_content')
                with open(download_path + image_name, 'wb') as f:
                    f.write(image_content)
                    print('下载成功:', image_name)
            else:
                print('类型不符合规定...')

    def close_spider(self, spider):
        if spider.name == "douban":
            self.mongo_client.close()