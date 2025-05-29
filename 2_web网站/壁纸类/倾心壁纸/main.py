import json
import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "origin": "https://bz.zhongerqiqi.cn",
    "priority": "u=1, i",
    "referer": "https://bz.zhongerqiqi.cn/",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
}
url = "https://api.zhongerqiqi.cn/index/bzzuopin/xinfenlei"
params = {
    "page": "13",
    "fenlei": "0",
    "choose": "0",
    "xifen": "0"
}
response = requests.get(url, headers=headers, params=params)
data = response.json()
import execjs
function_code=open('main.js',encoding='utf-8').read()
data_code=execjs.compile(function_code)
data_file=data_code.call('lank',data)
print(data_file)
