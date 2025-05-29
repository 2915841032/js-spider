
import time
import execjs
import requests
import base64

json_data = {
    'pageNo': 1,
    'pageSize': 20,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2022-10-10 00:00:00',
    'EndTime': '2023-04-10 23:59:59',
    'createTime': [],
    'ts': int(round(time.time() * 1000)),
}
JsFile = open('请求.js', encoding='gb18030')
JsCode = JsFile.read()
compile_JsCode = execjs.compile(JsCode)
ParameterData = compile_JsCode.call('d', json_data)

print(ParameterData)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5,fr;q=0.4,de;q=0.3',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://ggzyfw.fujian.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fujian.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'portal-sign': ParameterData,
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
response = requests.post('https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo', headers=headers, json=json_data)

# 读取 JavaScript 文件内容并指定编码（例如UTF-8）
with open('解密.js', 'r', encoding='gb18030') as file:
    javascript_code = file.read()
# 创建 Context 对象
context = execjs.compile(javascript_code)
result = context.call('main',str(response.json()['Data']))
decoded_result = base64.b64decode(result).decode('utf-8')
print(decoded_result)

