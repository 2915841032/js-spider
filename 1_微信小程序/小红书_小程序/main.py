import requests


headers = {
    "Host": "recruit.xiaohongshu.com",
    "xweb_xhr": "1",
    # "authorization": "tM335AvdZEA9Z715tiBHB2EgQRJw8ebIETqvBS4aQ3Q=",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/11581",
    "content-type": "application/json",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx6e18c5c45387efa2/51/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url = "https://recruit.xiaohongshu.com//recruit/wx/position/detail/13958"
response = requests.get(url, headers=headers)

print(response.text)
print(response)