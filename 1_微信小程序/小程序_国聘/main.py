import requests
import json


headers = {
    "Host": "gp-api.iguopin.com",
    "version": "3.0.14",
    "xweb_xhr": "1",
    "device": "wechat-mini",
    "subsite": "iguopin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/11581",
    "content-type": "application/json",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx451aea80e5b4bae8/37/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url = "https://gp-api.iguopin.com/api/jobs/v1/list"
data = {
    "page_size": 12,
    "with_hot": True,
    "page": 2
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)
with open('res.json', 'w', encoding='utf-8') as f:
    f.write(response.text)