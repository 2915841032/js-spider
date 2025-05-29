import json
import time

import pymongo
import requests
import hashlib
from loguru import logger
from redis.client import Redis
from jmespath import search


class Spider():
    def __init__(self):
        self.mongodb = pymongo.MongoClient()
        self.db = self.mongodb['spider']
        self.coll = self.db['court_auction']
        self.redis_cli = Redis()
        self.location_change = {
            'beiJin': {'locationCode': '110000',
                       'sid': '0272474869_1684412604030'},
            'shangHai': {
                'locationCode': '310000',
                'sid': '1373475548_1684412676879'
            },
            'guangZhou': {'locationCode': '440000',
                          'sid': '8608688863_1684412736958'}
        }

    def md5_enc(self, str):
        md5 = hashlib.md5()
        md5.update(str.encode('utf-8'))
        return md5.hexdigest()

    def get_cookie(self):
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'Referer': 'https://zc-paimai.taobao.com/',
        }
        params = (
            ('jsv', '2.6.1'),
            ('appKey', '12574478'),
            ('t', '1684378620773'),
            ('sign', '796d54577ac8db0af55dab2f0a06555d'),
            ('bxPageId', '1910955'),
            ('api', 'mtop.taobao.datafront.invoke.auctionwalle'),
            ('v', '1.0'),
            ('type', 'originaljson'),
            ('dataType', 'json'),
            ('requiredParams', 'dfApiName,dfUniqueId'),
        )
        data = {
            'data': '{"dfApp":"auctionwalle","dfApiName":"auctionwalle.datou.getPageModulesData","dfVariables":"{\\"pageId\\":1910955,\\"moduleIds\\":\\"4394607430,4489817680,4480874310,2004318340,4529967930,2708524060,global\\",\\"context\\":{\\"pmid\\":\\"7287198777_1684376275117\\",\\"pmtk\\":\\"20140647.0.0.0.27064540.puimod-pc-search-navbar_5143927030.vault-jump\\",\\"spm\\":\\"a2129.27064540.puimod-pc-search-navbar_5143927030.vault-jump\\",\\"path\\":\\"27064540\\",\\"keyword\\":\\"\u4E8C\u624B\u623F\\",\\"page\\":\\"2\\",\\"userInfo\\":\\"{}\\",\\"sceneCode\\":\\"20210823QCG72BUD\\",\\"firstScreen\\":\\"true\\",\\"device\\":\\"pc\\"}}","dfUniqueId":"1910955.4394607430,4489817680,4480874310,2004318340,4529967930,2708524060,global","dfVariablesRecover":"{}"}'
        }
        url='https://h5api.m.taobao.com/h5/mtop.taobao.datafront.invoke.auctionwalle/1.0/'
        logger.debug('url: ' + url)
        response = requests.post(url,headers=headers, params=params, data=data)
        logger.debug('cookie: ' + json.dumps(response.cookies.get_dict(), ensure_ascii=False, indent=2))
        return response.cookies.get_dict()

    def get_data(self, cookie, page, location):
        cur_timeStamp = str(round(time.time() * 1000))
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://zc-paimai.taobao.com/",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        url = "https://h5api.m.taobao.com/h5/mtop.taobao.datafront.invoke.auctionwalle/1.0/"
        logger.debug('url: ' + url)
        data = {
            "data": "{\"dfApp\":\"auctionwalle\",\"dfApiName\":\"auctionwalle.datou.getPageModulesData\",\"dfVariables\":\"{\\\"pageId\\\":1910955,\\\"moduleIds\\\":\\\"2004318340:items\\\",\\\"context\\\":{\\\"_b_2004318340:items\\\":\\\"{\\\\\\\"keyword\\\\\\\":\\\\\\\"二手房\\\\\\\",\\\\\\\"pmid\\\\\\\":\\\\\\\"3840625134_1684412570290\\\\\\\",\\\\\\\"pmtk\\\\\\\":\\\\\\\"20140647.0.0.0.27064540.puimod-pc-search-navbar_5143927030.vault-jump\\\\\\\",\\\\\\\"spm\\\\\\\":\\\\\\\"a2129.27064540.puimod-pc-search-navbar_5143927030.vault-jump\\\\\\\",\\\\\\\"path\\\\\\\":\\\\\\\"27064540\\\\\\\",\\\\\\\"locationCodes\\\\\\\":[\\\\\\\"%(locationCode)s\\\\\\\"],\\\\\\\"userInfo\\\\\\\":{},\\\\\\\"appendMap\\\\\\\":{\\\\\\\"sid\\\\\\\":\\\\\\\"%(sid)s\\\\\\\"},\\\\\\\"page\\\\\\\":\\\\\\\"%(page)s\\\\\\\"}\\\",\\\"userInfo\\\":\\\"{}\\\",\\\"device\\\":\\\"pc\\\",\\\"sceneCode\\\":\\\"20210823QCG72BUD\\\"}}\",\"dfUniqueId\":\"1910955.2004318340:items\",\"dfVariablesRecover\":\"{}\"}" % {
                'page': page, 'locationCode': location['locationCode'], 'sid': location['sid']}
        }
        params = {
            "jsv": "2.6.1",
            "appKey": "12574478",
            "t": cur_timeStamp,
            "sign": self.md5_enc(
                cookie['_m_h5_tk'].split('_', 1)[0] + "&" + cur_timeStamp + "&" + "12574478" + "&" + data[
                    'data']).encode(
                'utf-8'),
            "bxPageId": "1910955",
            "api": "mtop.taobao.datafront.invoke.auctionwalle",
            "v": "1.0",
            "type": "originaljson",
            "dataType": "json",
            "requiredParams": "dfApiName,dfUniqueId"
        }
        response = requests.post(url, headers=headers, cookies=cookie, params=params, data=data)
        return response

    def parse(self, res, city):
        data2save = []
        items = search('data.data.GQL_getPageModulesData."2004318340".items.schemeList', res.json())
        for item in items:
            title = search('auctionTitle', item)
            price = str(search('price', item)) + search('priceUnit', item)
            location = search('auctionBenefits', item)
            data2save.append({
                'city': city,
                'title': title,
                'price': price,
                'location': location
            })
        logger.debug('data: ' + json.dumps(data2save, indent=2, ensure_ascii=False))
        return data2save

    def save(self, data):
        """用redis set特性过滤避免重复插入,sadd如果有则返回1，否则是0"""
        for i in data:
            if self.redis_cli.sadd('court_auction', json.dumps(i)):
                self.coll.insert_one(i)
        logger.debug('保存成功!')

    def main(self):
        cookie = self.get_cookie()  # 这个cookie过期时间还挺长的,不用每次请求都变
        for k, v in self.location_change.items():
            for i in range(1, 2):
                res = self.get_data(cookie, i, v)
                data2save = self.parse(res, k)
                self.save(data2save)
                time.sleep(1)


if __name__ == '__main__':
    spider = Spider()
    spider.main()
