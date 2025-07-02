# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HcInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 你在spider类中的parse函数里定义的字段名必须和Item文件中定义的字段变量要保持一致
    announcementTitle = scrapy.Field()
    announcementTypeName = scrapy.Field()
    batchNum = scrapy.Field()
    secName = scrapy.Field()
    adjunctType = scrapy.Field()
