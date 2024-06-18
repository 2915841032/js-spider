import requests
import json
import execjs
data=open('请求.js',encoding='utf-8-sig').read()
res=execjs.compile(data).call('sign')
sign=res['sign']
timestamp=res['Timestamp']
print(len(sign),timestamp)
headers = headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://xk.scjgj.sh.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://xk.scjgj.sh.gov.cn/xzxk_wbjg/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sign": sign,
    "timestamp": timestamp
}
url = "https://xk.scjgj.sh.gov.cn/xzxk_wbjg/query/public/licInfo"
data = {
    "zszl": "00101,00102",
    "fzjg": "",
    "rows": 20,
    "page": 2
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)