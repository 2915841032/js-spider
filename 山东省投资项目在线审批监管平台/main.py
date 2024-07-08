import execjs
import requests
import json

function_code=open('参数生成.js',encoding='utf-8-sig').read()
data_code=execjs.compile(function_code)
data_file=data_code.call('main123')
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "http://221.214.94.51:8081",
    "Referer": "http://221.214.94.51:8081/icity/ipro/projectlist",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "X-Requested-With": "XMLHttpRequest"
}

url = data_file

data = {
    "projectcode": "",
    "projectname": "",
    "contractor": "",
    "projecttype": "",
    "page": 2,
    "limit": 10
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data, verify=False)

# print(response.text)
print(response)
data=response.json()['data']
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# print(response.json())