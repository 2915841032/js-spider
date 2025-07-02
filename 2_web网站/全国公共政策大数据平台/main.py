import requests
import execjs
import base64
data=open('请求加密.js','r',encoding='utf-8').read()
ctx = execjs.compile(data)
m={
    "policyType": "4",
    "province": "",
    "city": "",
    "downtown": "",
    "garden": "",
    "centralId": "",
    "sort": 0,
    "homePageFlag": 1,
    "pageNum": 1,
    "pageSize": 7
}

r = ctx.call('ank', m)
print(r)
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/octet-stream",
    "Origin": "https://www.spolicy.com",
    "Pragma": "no-cache",
    "Referer": "https://www.spolicy.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

url = "https://www.spolicy.com/info_api/policyType/showPolicyType"
# data = bytes(r['data'])
data = base64.b64decode(r)
response = requests.post(url, headers=headers,  data=data)

print(response.text)
print(response)