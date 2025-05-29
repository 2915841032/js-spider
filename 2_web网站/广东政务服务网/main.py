import requests
import execjs
datacode=open("请求.js", "r", encoding="utf-8").read()
ctx = execjs.compile(datacode)
code = ctx.call("lank")
# print(code)
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Data-Type": "16",
    "Origin": "http://203.91.46.83:8031",
    "Post-Type": "1",
    "Pragma": "no-cache",
    "RESPTYPE": "1",
    "Referer": "http://203.91.46.83:8031/FGWPM/sfg/wstb_qybs",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
}
cookies = {
    "JSESSIONID": "D7F4AADC79A75FD3632E04424EACFEE4"
}
url = "http://203.91.46.83:8031/FGWPM/LEAP/Service/RPC/RPC.DO"
params = {
    "callService": "web",
    "method": "fgwpm_getBusinessByType",
    "sid": "D7F4AADC79A75FD3632E04424EACFEE4",
    "_website_": "*",
    "parlen": "5"
}
data = {
    "a": code
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data, verify=False)

print(response)
print(response.text)
