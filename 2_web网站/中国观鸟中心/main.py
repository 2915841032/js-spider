import json

import requests
import execjs
datacode=open('test2.js', 'r', encoding='utf-8').read()
ctx = execjs.compile(datacode)
data= 'page=5&limit=20&taxonid=&startTime=&endTime=&province=%E9%9D%92%E6%B5%B7%E7%9C%81&city=&district=&pointname=&username=&serial_id=&ctime=&taxonname=&state=&mode=0&outside_type=0'

c=ctx.call('get_headers',data)
data=c['data']
c=c['headers']
# print(c['timestamp'])

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://www.birdreport.cn",
    "Pragma": "no-cache",
    "Referer": "http://www.birdreport.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "requestId": f"{c['requestId']}",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sign": f"{c['sign']}",
    "timestamp": f"{c['timestamp']}"
}
url = "https://api.birdreport.cn/front/record/activity/search"
# data = c['data']
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)
datacode2=open('解密.js', 'r', encoding='utf-8').read()
ctx2 = execjs.compile(datacode2)
data=ctx2.call('get_decrypted',response.json()['data'])
print(data)
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=4))
