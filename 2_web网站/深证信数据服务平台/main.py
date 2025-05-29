import requests
import execjs
jscode=open("2.js","r",encoding="utf-8").read()
ctx = execjs.compile(jscode)
md5 = ctx.call("getResCode")
print(md5)
headers = {
    "Accept": "*/*",
    "Accept-EncKey": f"{md5}",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://webapi.cninfo.com.cn",
    "Referer": "https://webapi.cninfo.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007"
data = {
    "tdate": "2025-02-25",
    "market": "SZE"
}
response = requests.post(url, headers=headers, data=data)

print(response.json())
print(response)

# 未完成，相关网址如下
# https://www.cnblogs.com/sbhglqy/p/18170153
