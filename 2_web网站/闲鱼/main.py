import json

import requests
import execjs
import time

# 初始化常量和数据
h = 34839810
data = {
    "data": "{\"itemId\":\"\",\"pageSize\":30,\"pageNumber\":2,\"machId\":\"168395_1\"}"
}
timestamp = int(time.time()) * 1000  # 获取当前时间戳（单位为毫秒）
# 拼接需要加密的字符串
need_encrypt_str = "1b4d7c1da0f7395354ee233a75b8e75d" + "&" + str(timestamp) + "&" + str(h) + "&" + data["data"]
# 读取并执行 JS 代码进行加密
with open("main.js", mode='r') as file:
    exec_js = file.read()
exec_code = execjs.compile(exec_js)
res = exec_code.call("i", need_encrypt_str)
# API 请求的 URL 和参数
url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlehome.home.webpc.feed/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "34839810",
    "t": str(timestamp),
    "v": "1.0",
    "type": "originaljson",
    "accountSite": "xianyu",
    "dataType": "json",
    "timeout": "20000",
    "api": "mtop.taobao.idlehome.home.webpc.feed",
    "sessionOption": "AutoLoginOnly",
    "spm_cnt": "a21ybx.home.0.0",
    "sign": res
}
# 请求头设置
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Content-Length": "109",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.goofish.com",
    "Referer": "https://www.goofish.com/",
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    "Sec-Ch-Ua-Mobile": "?0",
    'Sec-Ch-Ua-Platform': '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}
cookies = {
    "cookie2": "1a00795d55ec285f988a8f33ca8cdc50",
    "sgcookie": "E100fdzIZO6yHuwMUF6GHDKP1R14D9MlQwYkFjKLBJX7rd1ChRfpmoJEwzU1xon46reh3%2BSt891hSBmGCG%2B%2F6uan6vQnYIAi0jiZWcEfEcpCkIyuLJthUX%2FYDOgnA2ptwkwT",
    "_m_h5_tk": "1b4d7c1da0f7395354ee233a75b8e75d_1746168275538",
    "_m_h5_tk_enc": "fd6af780415b6c27cfe5e22595d05d57"
}

response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)

with open("response.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(response.json(), ensure_ascii=False, indent=4))