import requests
import execjs


class YibBao():
    def __init__(self):
        self.headers = {
            "Accept": "application/json",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://fuwu.nhsa.gov.cn",
            "Pragma": "no-cache",
            "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
            "channel": "web",
            "contentType": "application/x-www-form-urlencoded",
            "sec-ch-ua-mobile": "?0",
            "x-tif-paasid": "undefined",
        }
        self.url = 'https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital'
        self.js = execjs.compile(open('02-医保.js', encoding='utf-8').read())
        self.data = {
            "data": {
                "addr": "",
                "regnCode": "430100",
                "medinsName": "",
                "medinsLvCode": "",
                "medinsTypeCode": "",
                "openElec": "",
                "pageNum": 10,
                "pageSize": 10,
                "queryDataSource": "es"
            },
            "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
            "version": "1.0.0",
            "encType": "SM4",
            "signType": "SM2",
            "timestamp": 1706101448
        }

    def get_data(self, i):

        head = self.js.call('get_headers')
        print(head)
        self.headers['x-tif-nonce'] = head['x-tif-nonce']
        self.headers['x-tif-paasid'] = 'undefined'
        self.headers['x-tif-signature'] = head['x-tif-signature']
        self.headers['x-tif-timestamp'] = str(head['x-tif-timestamp'])
        self.headers['X-Tingyun'] = head['X-Tingyun']
        # print(self.headers)
        self.data['timestamp'] = head['x-tif-timestamp']
        self.data['data']['pageNum'] = i
        data = self.js.call('json_data', self.data)
        # print(data)
        data1 = {"data": {"data": {
            "encData": data['encData']},
                          "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ", "version": "1.0.0", "encType": "SM4",
                          "signType": "SM2", "timestamp": head['x-tif-timestamp'],
                          "signData": data['signData']}}
        # print(data1)
        res = requests.post(self.url, headers=self.headers, json=data1)
        return res.json()

    def parse_data(self, data):
        res = self.js.call('parse_data', data)
        print(res)


    def main(self):
        for i in range(1, 10):
            data = self.get_data(i)
            self.parse_data(data)

if __name__ == '__main__':
    yb = YibBao()
    yb.main()
