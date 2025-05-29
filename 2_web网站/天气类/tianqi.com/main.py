import requests
import execjs
function_code=open('main.js',encoding='utf-8').read()
data_code=execjs.compile(function_code)

data_file=data_code.call('encrypt')

print(data_file)

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://lishi.tianqi.com",
    "priority": "u=1, i",
    "referer": "https://lishi.tianqi.com/changshaxian/202406.html",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
url = "https://lishi.tianqi.com/monthdata/changshaxian/202406"

data = {
    "crypte": f"{data_file}",
}
response = requests.post(url, headers=headers, data=data)

print(response.json())
print(response)