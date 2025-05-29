import requests


headers = {
    "Host": "xsbl.website",
    "xweb_xhr": "1",
    "source-client": "miniapp",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/11581",
    "token": "",
    "content-type": "application/json",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wxf36aa1fb857d2ec5/11/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url = "https://xsbl.website/user/showCategoryPage/getShowCategoryImage"
params = {
    "id": "2",
    "page": "6",
    "pageSize": "12"
}
response = requests.get(url, headers=headers, params=params)

print(response.json())
print(response)