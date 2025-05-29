import requests
import time
# 实现md5标准加密
import hashlib
time=int(time.time()*1000)
start_str=f"pageindex=6&pagesize=30&timestamp={time}&userid=23088682053ef899Af294A36bB5ae1730c7995E8"
md5 = hashlib.md5()
md5.update(start_str.encode('utf-8'))
print(md5.hexdigest())


headers = {
    "authority": "minibizhi.313515.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "deviceinfo": "CH=1&Height=622&Lang=zh_CN&Model=microsoft&Net=unknown&PID=1&PixelRatio=1.25&SignatureStamp=1741958585536&Ver=2&Version=3.9.10&Width=415&SignatureMD5=6ef63c2b43e8fb3be78230ceb7069a2b",
    "referer": "https://servicewechat.com/wxd521f27d130179fa/386/page-frame.html",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
    "xweb_xhr": "1"
}
url = "https://minibizhi.313515.com/list/background"
params = {
    "pageindex": "6",
    "pagesize": "30",
    "userID": "23088682",
    "timeStamp": f"{time}",
    "SignatureMD5": f"{md5.hexdigest()}"
}
response = requests.get(url, headers=headers, params=params)

print(response.json())
print(response)