import requests
import execjs
datacode=open('main.js','r',encoding='utf-8').read()
ctx = execjs.compile(datacode)
sb = ctx.call('lb')
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "client": "web",
    "coinank-apikey": f"{sb}",
    "content-length": "0",
    "origin": "https://coinank.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://coinank.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "token;": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    "web-version": "101"
}
url = "https://api.coinank.com/api/fund/fundReal"
params = {
    "page": "1",
    "size": "50",
    "type": "1",
    "productType": "SPOT",
    "sortBy": "",
    "baseCoin": "",
    "isFollow": "false"
}
response = requests.post(url, headers=headers, params=params)

print(response.text)
print(response)

with open('data.json', 'w', encoding='utf-8') as f:
    f.write(response.text)