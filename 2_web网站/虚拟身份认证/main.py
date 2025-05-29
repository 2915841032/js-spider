import requests


headers = {
    "Host": "www.sunzhongwei.com",
    "xweb_xhr": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/11581",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx9e2129a47295750f/59/page-frame.html",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
url = "https://www.sunzhongwei.com/api/getRandomPersonInfo"
params = {
    "key": "sunzhongwei.com"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)