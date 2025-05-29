import requests


headers = {
    "Accept": "*/*",
    "Accept-EncKey": "C9vlYbxjkmnT8AdW+mtIcA==",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://webapi.cninfo.com.cn",
    "Pragma": "no-cache",
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

print(response.text)
print(response)