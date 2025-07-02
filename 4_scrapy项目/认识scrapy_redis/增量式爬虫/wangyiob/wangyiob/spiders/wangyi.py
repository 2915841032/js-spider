import json

import scrapy
from scrapy.http import JsonRequest


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    allowed_domains = ["hr.163.com"]

    def start_requests(self):
        api_url = 'https://hr.163.com/api/hr163/position/queryPage'
        for page in range(1, 100):
            json_data = {
                'currentPage': page,
                'pageSize': 10
            }
            yield JsonRequest(api_url, data=json_data)

    def parse(self, response, **kwargs):
        for info_list in response.json()['data']['list']:
            item = {}  # 启用items文件进行数据验证
            item['id'] = info_list['id']
            item['name'] = info_list['name']
            item['firstPostTypeName'] = info_list['firstPostTypeName']
            item['reqEducationName'] = info_list['reqEducationName']
            item['reqWorkYearsName'] = info_list['reqWorkYearsName']
            item['type'] = 'info'

            print(item)
            yield item

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute(['scrapy', 'crawl', 'wangyi'])
