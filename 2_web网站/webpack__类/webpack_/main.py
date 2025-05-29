import time

import requests
import execjs
datacode=open("main.js",encoding='utf-8-sig').read()
ctx = execjs.compile(datacode)
datatime=int(time.time()*1000)
m = ctx.call("main",datatime)
print(m)

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/16",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1744120583",
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1744120584",
    "sessionid": "4z0clg5o35nhrgpnzupbmng6per5wgl5",
    "no-alert3": "true",
    "tk": "2810045434979349368"
}
url = "https://match.yuanrenxue.cn/api/match/16"
params = {
    "page": "3",
    "m": f"{m['m']}",
    "t": f"{m['time']}"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)