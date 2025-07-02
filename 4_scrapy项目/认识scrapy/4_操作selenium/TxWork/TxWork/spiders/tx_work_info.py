from typing import Iterable

import redis
import hashlib
import scrapy
from scrapy import cmdline


class TxWorkInfoSpider(scrapy.Spider):
    name = "tx_work_info"
    allowed_domains = ["careers.tencent.com"]

    # start_urls = ["https://careers.tencent.com/search.html"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis_client = redis.Redis()

    def __del__(self):
        self.redis_client.close()

    # 父类中的start_requests方法默认不过滤重复的url
    def start_requests(self):
        url = 'https://careers.tencent.com/search.html?index={}&keyword=python'
        for page in range(1, 6):
            md5_hash = hashlib.md5()
            md5_hash.update(url.format(page).encode())
            hash_value = md5_hash.hexdigest()

            if self.redis_client.get(f'tx_work_url_filter: {hash_value}'):
                print('url重复...')
                continue
            else:
                self.redis_client.set(f'tx_work_url_filter: {hash_value}', url.format(page))

            yield scrapy.Request(url=url.format(page))

    def parse(self, response, **kwargs):
        div_list = response.xpath("//div[@class='correlation-degree']/div/div")
        for div in div_list:
            item = dict()
            item['title'] = div.xpath('./a//span[@class="job-recruit-title"]/text()').extract_first()
            item['department'] = div.xpath('./a/p[1]/span[1]/text()').extract_first()
            item['address'] = div.xpath('./a//span[2]/text()').extract_first()
            item['post'] = div.xpath('./a/p[1]/span[3]/text()').extract_first()
            item['date'] = div.xpath('./a/p[1]/span[last()]/text()').extract_first()
            item['recruit_data'] = div.xpath('./a/p[2]/text()').extract_first()
            yield item


if __name__ == '__main__':
    cmdline.execute('scrapy crawl tx_work_info'.split())
