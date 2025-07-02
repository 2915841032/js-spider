import time

# import requests
from curl_cffi import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://htgs.ccgp.gov.cn/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5": f"{int(time.time())-1}",
    "Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5": f"{int(time.time())}"
}
url = "http://download.ccgp.gov.cn/oss/download"
params = {
    "uuid": "d1109d5e-b298-4bb4-9746-143af5"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)

# print(response.text)
# print(response)
with open('4.pdf', 'wb') as f:
    f.write(response.content)