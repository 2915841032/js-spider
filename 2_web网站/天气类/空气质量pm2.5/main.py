import csv
import json

import execjs
import requests

headers = {
    "Accept": "image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.aqistudy.cn",
    "Pragma": "no-cache",
    "Referer": "https://www.aqistudy.cn/",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

url = "https://www.aqistudy.cn/apinew/aqistudyapi.php"

function_code=open('请求.js',encoding='utf-8-sig').read()
data_code=execjs.compile(function_code)
m0fhOhhGL="GETDATA"
oNLhNQ={'city': "北京"}
data_file=data_code.call('lk',m0fhOhhGL,oNLhNQ)
# print(data_file)

data = {
    "hXhY1B2Kd": data_file
}
response = requests.post(url, headers=headers, data=data)
# print(response.text)
# print(response.status_code)
function_code=open('解密.js',encoding='utf-8-sig').read()
data_code=execjs.compile(function_code)
data_file=data_code.call('deIZLF7oahc0DLiXbqt',response.text)
# print(data_file)
data=json.loads(data_file)
data=data['result']['data']['rows']
print(data)
with open('结果文件.csv','a',encoding='utf-8-sig',newline='')as f:
    writer=csv.DictWriter(f,data[0].keys())
    if f.tell()==0:
        writer.writeheader()
    writer.writerows(data)

print('ok')
