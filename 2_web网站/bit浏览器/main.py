import requests
import execjs
jscode=open("main.js","r",encoding="utf-8").read()
ctc=execjs.compile(jscode)
ctx=ctc.call("get_id")
print(ctx)
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "app-type": "web",
    "priority": "u=1, i",
    "referer": "https://www.oklink.com/zh-hans/btc/tx-list/page/4",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "x-apikey": f"{ctx['bb']}",
    "x-cdn": "https://static.oklink.com",
    "x-locale": "zh_CN",
    "x-site-info": "9FjOikHdpRnblJCLiskTJx0SPJiOiUGZvNmIsIiTDJiOi42bpdWZyJye",
    "x-utc": "8",
    "x-zkdex-env": "0"
}
url = "https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict"
params = {
    "offset": "60",
    "limit": "20",
    "t": f"{ctx['v']}"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)