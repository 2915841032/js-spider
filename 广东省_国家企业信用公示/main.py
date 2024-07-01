import time

import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://gsxt.amr.gd.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://gsxt.amr.gd.gov.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

url = "https://gsxt.amr.gd.gov.cn/gsxt_gd/captcha/get"
data = {
    "captchaType": "blockPuzzle",
    "clientUid": "slider-89577a95-d64f-45aa-8352-fc3e21ee70f8",
    "ts": int(time.time()*1000)
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers,  data=data)

print(response.text)
# print(response)