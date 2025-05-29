import json

import requests


headers = {
    "Host": "zpwechat.58.com",
    # "lon": "112.81790161132812",
    "source": "0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/11581",
    "content-type": "application/json",
    "xweb_xhr": "1",
    # "openid": "oBIU_5WGKoHPRFxfo9Fkn9AMMm44",
    # "lat": "28.361209869384766",
    "appid": "wxa9a9dec97e6ee639",
    "platform": "miniprogram",
    "spm": "",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wxa9a9dec97e6ee639/391/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}

url = "https://zpwechat.58.com/api/mixList"
params = {
    "scene": "homepage",
    "type": "jobList",
    "cityId": "414",
    "localId": "414",
    "page": "7",
    "pageSize": "50",
    "tagParams": "{\"tagresult\":[{\"tagName\":\"Python开发\",\"tagid\":\"413801\",\"tagType\":\"ncate\",\"tagPos\":\"1\",\"tagSourceType\":\"userSelectByJianLi\",\"selected\":1,\"childTabs\":[{\"tagName\":\"最新\",\"tagid\":\"-1\",\"tagType\":\"newChildTab\",\"selected\":1}]}],\"childTab\":[{\"tagName\":\"最新\",\"tagid\":\"-1\",\"tagType\":\"newChildTab\",\"selected\":1}],\"cmcstitle\":\"\",\"prepid\":\"\"}",
    "pid": "808832695419305984"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)
with open('res.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(response.json(), ensure_ascii=False, indent=4))
