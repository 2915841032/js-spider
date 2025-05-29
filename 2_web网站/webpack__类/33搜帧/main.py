import json

import requests
import execjs
import time
datacode=open('test2.js',encoding='utf-8').read()
ctx = execjs.compile(datacode)
time_=int(time.time()*1000)
res=ctx.call('lank()', f"_platform=web,_ts={time_},_versioin=0.2.5,keyword=火车呼啸而过,limit=12,page=1,")


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://fse.agilestudio.cn",
    "Pragma": "no-cache",
    "Referer": "https://fse.agilestudio.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "X-Signature": f"{res}",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://fse-api.agilestudio.cn/api/search"
params = {
    "keyword": "火车呼啸而过",
    "page": "1",
    "limit": "12",
    "_platform": "web",
    "_versioin": "0.2.5",
    "_ts": f"{time_}"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)

with open('result.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(response.json(), ensure_ascii=False, indent=4))
print('done')