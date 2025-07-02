import requests


headers = {
    "Host": "www.zhipin.com",
    "mini_ver": "13.0801",
    "ua": "{\"model\":\"microsoft\",\"platform\":\"windows\"}",
    # "wt2": "EuTetNsahHAu3iJbivjPJAl58gtxUlJuuXq_hdFpHvH80W4CfAhFosEA22mQtF5Zv1QvQpFkvCM8cX3d0FFk_dA~~",
    "zp_app_id": "10002",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/13639",
    "content-type": "application/x-www-form-urlencoded",
    "traceid": "F-e155cfYrw1zYwklI",
    # "mpt": "17c70df3677f95696cfeefcf03c5f07e",
    "scene": "1005",
    "xweb_xhr": "1",
    "x-requested-with": "XMLHttpRequest",
    "zp_product_id": "10002",
    "platform": "zhipin/windows",
    "ver": "13.0801",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wxa8da525af05281f3/559/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1, i",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
url = "https://www.zhipin.com/wapi/batch/batchRunV3"
params = {
    "batch_method_feed": "[\"method=/wapi/zpgeek/miniapp/job/detail.json&securityId=tYDQSOKco76By-d1WISYMuHoz338rDRV-OZpzmke_NLdRebFsQfyWkNSzW6XiM7cD4ysWu6JOA0NYou9jgKdU-Yb7r3F&jobId=7d02184c57bd910a03Z72tW8EVFY&lid=8IPTbkWT401.search.1&source=11&scene=\",\"method=/wapi/zpgeek/miniapp/jobdetail/improvement/query.json&securityId=tYDQSOKco76By-d1WISYMuHoz338rDRV-OZpzmke_NLdRebFsQfyWkNSzW6XiM7cD4ysWu6JOA0NYou9jgKdU-Yb7r3F&jobId=7d02184c57bd910a03Z72tW8EVFY&lid=8IPTbkWT401.search.1&source=11&scene=\"]",
    "appId": "10002"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)