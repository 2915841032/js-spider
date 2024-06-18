# https://www.qimingpian.com/finosda/project/ainvestment


import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.qimingpian.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'time_interval': '',
    'industry': '',
    'page': '1',
    'num': '20',
    'unionid': '',
}

response = requests.post('https://vipapi.qimingpian.cn/DataList/investmentTotalVip', headers=headers, data=data).json()
encrypt_data=response['encrypt_data']


import execjs

# 读取 JavaScript 文件内容
with open('1.js', 'r', encoding='utf-8') as file:
    javascript_code = file.read()

# 创建 Context 对象
context = execjs.compile(javascript_code)

# 执行 JavaScript 代码
result = context.call('s', encrypt_data)

print(result)