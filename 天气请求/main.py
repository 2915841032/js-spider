# -*- coding: utf-8 -*-

import base64
import csv
import json

import requests
import execjs

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
}

url = "https://www.aqistudy.cn/historydata/api/historyapi.php"
function_code=open('请求.js',encoding='utf-8').read()
data_code=execjs.compile(function_code)

m0fhOhhGL="GETDAYDATA"
oNLhNQ={'city': "北京", 'month': "201401"}
data_file=data_code.call('data_post',m0fhOhhGL,oNLhNQ)

data = {
    "hA4Nse2cT": data_file
}
response = requests.post(url, headers=headers, data=data)

# print(response.text)
print(response.status_code)


function_code=open('解密.js','r',encoding='utf-8-sig').read()
data_code=execjs.compile(function_code)
data_file=data_code.call('dxvERkeEvHbS',response.text)

# data_file=eval(data_file)
# print(data_file)
# print(eval(data_file.encode('utf-8').decode('utf-8')))
da=json.loads(data_file)
# print(da)
res=da['result']['data']['items']
with open('结果.csv','w',encoding='gb18030',newline='')as f:
  writer=csv.DictWriter(f,res[0].keys())
  writer.writeheader()
  writer.writerows(res)
print('ok')