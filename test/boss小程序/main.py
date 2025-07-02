import requests


headers = {
    "Host": "www.zhipin.com",
    "mini_ver": "13.0903",
    "ua": "{\"model\":\"microsoft\",\"platform\":\"windows\"}",
    # "wt2": "EuTetNsahHAu3iJbivjPJAl58gtxUlJuuXq_hdFpHvH80W4CfAhFosEA22mQtF5Zv1QvQpFkvCM8cX3d0FFk_dA~~",
    "zp_app_id": "10002",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/13639",
    "content-type": "application/x-www-form-urlencoded",
    # "traceid": "F-a73069iy2GBzWD4J",
    "mpt": "2d4d4bcbdd7f8662b87c1b1d2dc25836",
    "scene": "1005",
    "xweb_xhr": "1",
    "x-requested-with": "XMLHttpRequest",
    "zp_product_id": "10002",
    "platform": "zhipin/windows",
    "ver": "13.0903",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wxa8da525af05281f3/563/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1, i",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
url = "https://www.zhipin.com/wapi/zpgeek/miniapp/search/joblist.json"
params = {
    "pageSize": "15",
    "query": "数据分析",
    "city": "101250100",
    "source": "1",
    "sortType": "0",
    "subwayLineId": "",
    "subwayStationId": "",
    "districtCode": "",
    "businessCode": "",
    "longitude": "",
    "latitude": "",
    "position": "",
    "expectId": "",
    "expectPosition": "",
    "encryptExpectId": "6dc6a90fa03b58c40XF80tu_EVFW",
    "experience": "102,108",
    "page": "4",
    "appId": "10002"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)