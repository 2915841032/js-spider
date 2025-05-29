import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Referer": "https://servicewechat.com/wxcbfa127f857c2790/512/page-frame.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "SecretKey": "94cbe78f3bcec8be81d68e7bdfb9ad9b",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
    "id": "0",
    "platform": "1",
    "tradeid": "1000",
    "uid": "0",
    "xweb_xhr": "1"
}
url = "https://api.yl1001.com/webservice/index.php"
params = {
    "op": "zp_info_busi",
    "func": "searchZp",
    "version": "v7.8.7",
    "rtype": "json",
    "SYS_CACHE_FLAG": "0",
    "gtype": "http",
    "secret": "aXBob25l",
    "access_token": "de5d646ba333f24661d4dcb41f67b730"
}
data = {
    "tradeid": "1000",
    "queryItemArr": "{\"regionid\":\"\",\"salary\":\"\",\"gznum\":\"\",\"itime_num\":\"\",\"eduId\":\"\",\"jobtypes\":\"\"}",
    "conditionArr": "{\"page\":2,\"page_size\":10}"
}
response = requests.post(url, headers=headers, params=params, data=data)

print(response.json())
print(response)