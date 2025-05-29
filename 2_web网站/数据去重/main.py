import redis
import pymongo
import hashlib
import requests


class MovieInfo:
    def __init__(self):
        self.headers ={
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "origin": "https://www.mgtv.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.mgtv.com/",
            "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
        }
        self.api_url = "https://pianku.api.mgtv.com/rider/list/pcweb/v3"

        self.mongo_client = pymongo.MongoClient(
            "mongodb://root:root@localhost:27017/",
            authSource='admin',  # 通常认证数据库是admin
            authMechanism='SCRAM-SHA-256'  # 使用更新的认证机制
        )
        self.collection = self.mongo_client['py_spider']['mg_info']
        self.redis_client = redis.Redis()

    # 请求数据
    def get_movie_info(self, params):
        response = requests.get(self.api_url, headers=self.headers, params=params)
        print(response.text)
        return response.json()

    # 数据清洗以及数据结构调整
    def parse_movie_data(self, response):
        movie_list = response['data']['hitDocs']
        print(len(movie_list))
        for movie in movie_list:
            item = dict()
            item['title'] = movie['title']
            item['subtitle'] = movie['subtitle']
            item['story'] = movie['story']
            self.save_movie_info(item)

    # 数据去重
    @staticmethod
    def get_md5(item):
        md5_hash = hashlib.md5(str(item).encode('utf-8')).hexdigest()
        return md5_hash

    # 数据保存
    def save_movie_info(self, item):
        value = self.get_md5(item)
        # 当前集合的key如果有冒号, redis会在内部创建一个文件夹
        result = self.redis_client.sadd('movie:filter', value)

        # 如果md5可以正确保存到redis中则返回1, 否则返回0
        if result:
            self.collection.insert_one(item)
            print('保存成功: ', item)
        else:
            print('数据重复...')

    # 启动方法
    def main(self):
        for page in range(4, 10):
            params = {
                "allowedRC": "1",
                "platform": "pcweb",
                "channelId": "2",
                "pn": "2",
                "pc": f"{page}",
                "hudong": "1",
                "_support": "10000000",
                "kind": "19",
                "area": "10",
                "year": "all",
                "chargeInfo": "a1",
                "sort": "c2",
                "feature": "all"
            }
            response = self.get_movie_info(params)
            self.parse_movie_data(response)


if __name__ == '__main__':
    movie_info = MovieInfo()
    movie_info.main()
