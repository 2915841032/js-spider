import scrapy
import json
from scrapy.http import JsonRequest
from scrapy_redis.spiders import RedisSpider


class WangyiSpider(RedisSpider):
    name = "wangyi"
    allowed_domains = ["hr.163.com"]
    redis_key = "wangyi:start_urls"  # 指定Redis队列键名

    # 重写请求生成方法
    def make_request_from_data(self, data):
        # 解析Redis队列中的JSON数据
        task = json.loads(data)
        page = task.get('page', 1)

        # 构造API请求
        api_url = "https://hr.163.com/api/hr163/position/queryPage"
        json_data = {
            'currentPage': page,
            'pageSize': 10
        }
        return JsonRequest(
            url=api_url,
            data=json_data,
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, response, **kwargs):
        try:
            data = response.json()
            work_list = data['data']['list']

            for work in work_list:
                yield {
                    'work_id': str(work['id']),
                    'name': work['name'],
                    'firstPostTypeName': work['firstPostTypeName'],
                    'requirement': work['requirement'],
                }
        except (KeyError, json.JSONDecodeError) as e:
            self.logger.error(f"解析错误: {e} - 响应内容: {response.text[:200]}")
