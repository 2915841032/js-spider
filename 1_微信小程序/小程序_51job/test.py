import time
import requests
import json
import execjs
date=int(time.time())
# date=1744200197
key="abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b"
h=f'/open/noauth/recommend/job-tab-dynamic-wx-mini?api_key=51job&timestamp={date}{{"pageNo":7,"pageSize":50,"requestId":"9496bca120ce3763af3f98e30bd4652c","specialPageCode":true,"type":"recommend","jobArea":"190200"}}'
datacode=open('main.js','r',encoding='utf-8').read()
ctx = execjs.compile(datacode)
sign = ctx.call('hmacSHA256', key, h)
print(sign)
headers = {
    "authority": "cupid.51job.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "account-id": "260122417",
    "content-type": "application/json",
    "from-domain": "51job_weixin_wxapp",
    "partner;": "",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sign": f"{sign}",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
    "xweb_xhr": "1"
}
url = "https://cupid.51job.com/open/noauth/recommend/job-tab-dynamic-wx-mini"
params = {
    "api_key": "51job",
    "timestamp": f"{date}"
}
data = {
    "pageNo": 7,
    "pageSize": 50,
    "requestId": "9496bca120ce3763af3f98e30bd4652c",
    "specialPageCode": True,
    "type": "recommend",
    "jobArea": "190200"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)

with open('res1.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(response.json(), indent=4, ensure_ascii=False))