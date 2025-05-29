import requests
import execjs
from req_data import req
data_=req()

datacode=open('请求和解密.js','r',encoding='utf-8').read()
ctx = execjs.compile(datacode)

code = ctx.call('a',data_['code'])
headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=utf-8",
    "Pragma": "no-cache",
    "Referer": "https://www.ycjsjg.net/xxgs/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://www.ycjsjg.net/ycdc/bakCmisYcOrgan/getCurrentIntegrityPage"
params = {
    "pageSize": "10",
    "cioName": "公司",
    "page": "0",
    "code": f"{code}",
    "codeValue": f"{data_['time']}"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
# print(response)
res=ctx.call('a',response.json()['data'])
with open('res.json','w',encoding='utf-8') as f:
    f.write(res)
# print(res)