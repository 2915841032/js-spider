import requests
import json
import execjs
plan='{"sort":1,"start":140,"limit":20}'

datacode=execjs.compile(open('main.js').read()).call('lank',plan)
payload=datacode['payload']
sig=datacode['sig']

print(sig,payload)
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/json",
    "origin": "https://www.xiniudata.com",
    "priority": "u=1, i",
    "referer": "https://www.xiniudata.com/industry/newest?from=data",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}
url = "https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort"
data = {
    "payload": f"{payload}",
    "sig": f"{sig}",
    "v": 1
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers,  data=data)
print(response.json())

rescode=execjs.compile(open('main2.js').read()).call('lank2',str(response.json()['d']))
print(rescode)