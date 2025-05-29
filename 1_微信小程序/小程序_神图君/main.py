import time

import requests
import json
import execjs
jscode=open("main.js","r",encoding="utf-8").read()
ctx = execjs.compile(jscode)
a="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuaWQiOiJvZmcwSjVSbjN2MERCd0dWZ3JOQTd1U0VjM2JjIiwiZXhwaXJlX3RpbWUiOjE3NDE0Mjg5NTZ9.BTtgSL3ni5u6qhLpjsPGLgMQ6qwh7xcaJPalQBBQSvk"

end=ctx.call("s",a)



headers = {
    "authority": "stapi.youpengw.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "referer": "https://servicewechat.com/wxba7de3a24a3ff4d5/45/page-frame.html",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sign": end,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
    "xweb_xhr": "1"
}
url = "https://stapi.youpengw.com/miniwechat/v1/shentujun/photoList"
data = {
    "homepage_id": "159559",
    "classify_id": 5,
    "sort_type": "default",
    "album_id": 0,
    "uid": 153191,
    "page": 3,
    "limit": 15,
    "action": "cover",
    "version": 1,
    "appid": "wxba7de3a24a3ff4d5",
    "openid": "ofg0J5Rn3v0DBwGVgrNA7uSEc3bc",
    "timestamp": time.time()*1000
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)