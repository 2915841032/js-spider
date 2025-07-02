import json
import time

import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://snake.timeline.ink",
    "Pragma": "no-cache",
    "Referer": "https://snake.timeline.ink/latest",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Timeline-Client": "timelineweb",
    "Timeline-Device": "a94b3d8db6c0620d992588c2ae26b38f",
    "Timeline-Pwd;": "",
    "Timeline-User;": "",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://api.nguaduot.cn/snake/v4"
params = {
    "order": "date",
    "seed": f"{int(time.time()*1000)}",
    "no": "43589",
    "id": ""
}
response = requests.get(url, headers=headers, params=params)

# print(response.text)
# print(response)
with open("data.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(response.json(), ensure_ascii=False, indent=4))
print("写入完成")