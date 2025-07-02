import scrapy
# 导入模型
from scrapy import cmdline


class HcInfoDataSpider(scrapy.Spider):
    name = "HcInfoData"
    allowed_domains = ["www.cninfo.com.cn"]

    # start_urls = ["http://www.cninfo.com.cn/new/disclosure"]

    def start_requests(self):
        url = 'http://www.cninfo.com.cn/new/disclosure'
        for page in range(1, 3):
            data = {
                'column': 'szse_latest',
                'pageNum': str(page),
                'pageSize': '30',
                'sortName': '',
                'sortType': '',
                'clusterFlag': 'true',
            }
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    def parse(self, response, **kwargs):
        for info_list in response.json()['classifiedAnnouncements']:
            for info in info_list:
                item = {} # 启用items文件进行数据验证
                item['announcementTitle'] = info['announcementTitle']
                item['announcementTypeName'] = info['announcementTypeName']
                item['batchNum'] = info['batchNum']
                item['secName'] = info['secName']
                item['adjunctType'] = info['adjunctType']
                print(item)
                yield item


if __name__ == '__main__':
    cmdline.execute('scrapy crawl HcInfoData'.split())
