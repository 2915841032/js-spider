import requests
import json
import time

class JianZhu():
    def __init__(self):
        self.url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list?pg={}&pgsz=15&total=450"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            'Referer':'https://jzsc.mohurd.gov.cn/data/company',
            'V':'231012'
        }

    def get_Data(self, page):
        res = requests.get(self.url.format(page), headers=self.headers)
        return res.text

    def parse_Data(self, data):
        data = {
            "group": "rpc-test",
            "action": "jz",
            'data': data

        }
        # time.sleep(3)
        res = requests.post(url="http://127.0.0.1:5620/business-demo/invoke", data=data, verify=False)
        # print(res.json())
        if res.json().get('data'):
            print(res.json()['data'])
            #   保存数据
            with open('jz.txt', 'a', encoding='utf-8') as f:
                f.write(res.json()['data'] + '\n')


        else:
            print('连接问题')

    def main(self):
        for i in range(1, 5):
            data = self.get_Data(i)
            self.parse_Data(data)

if __name__ == '__main__':
    jz = JianZhu()
    jz.main()