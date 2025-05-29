import time

import requests
import json


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://funddb.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36 Edg/135.0.0.0"
}
url = "https://api.jiucaishuo.com/v2/fund-lists/fundpcrank"
data = {
    "cate_id": "",
    "type_id": 1,
    "order_by": "desc",
    "filed": "fund_income_12",
    "page": 4,
    "page_size": 100,
    "data_source": "jq",
    "type": "pc",
    "version": "2.2.7",
    "authtoken": "",
    "act_time": int(time.time()*1000),
    "tirgkjfs": "a6",
    "abiokytke": "55",
    "u54rg5d": "d4",
    "kf54ge7": "0",
    "tiklsktr4": "6",
    "lksytkjh": "8b97",
    "sbnoywr": "1b",
    "bgd7h8tyu54": "0b",
    "y654b5fs3tr": "4",
    "bioduytlw": "6",
    "bd4uy742": "7",
    "h67456y": "28b",
    "bvytikwqjk": "0b",
    "ngd4uy551": "8b",
    "bgiuytkw": "9e",
    "nd354uy4752": "2",
    "ghtoiutkmlg": "444",
    "bd24y6421f": "b9",
    "tbvdiuytk": "2",
    "ibvytiqjek": "85",
    "jnhf8u5231": "9e",
    "fjlkatj": "d4a",
    "hy5641d321t": "97",
    "iogojti": "9",
    "ngd4yut78": "44",
    "nkjhrew": "7",
    "yt447e13f": "5",
    "n3bf4uj7y7": "b",
    "nbf4uj7y432": "55",
    "yi854tew": "32",
    "h13ey474": "320",
    "quikgdky": "20"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)
with open("res.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(response.json()['data'], ensure_ascii=False, indent=4))