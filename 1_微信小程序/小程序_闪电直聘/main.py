import requests
import execjs
datacode=open("test.js","r",encoding="utf-8").read()
res=execjs.compile(datacode).call("calculateSignature")
sign=res['hex']
timestamp=res['time']

headers = {
    "authority": "mapi.mini.jgjapp.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "authorization": "WEAPP",
    "channel": "yzgong",
    "client-type": "person",
    "client_type": "person",
    "content-type": "application/json",
    "mini_os": "1",
    "miniprogram": "miniprogram",
    "os": "WEAPP",
    "package-name": "com.jizhi.jlongg.scllzh",
    "package_name": "com.jizhi.jlongg.scllzh",
    "platform": "weapp",
    "referer": "https://servicewechat.com/wx4c100b1c06ee0d1b/16/page-frame.html",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sign": f"{sign}",
    "timestamp": f"{timestamp}",
    "token;": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
    "ver": "7.3.20",
    "xweb_xhr": "1"
}
url = "https://mapi.mini.jgjapp.com/service/jobs/mix"
params = {
    "city_code": "0",
    "work_type": "493",
    "sort": "1",
    "pg": "1",
    "from": "1",
    "is_insert_head": "0",
    "pagesize": "20",
    "sess_data": "",
    "rule_id": "0"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)