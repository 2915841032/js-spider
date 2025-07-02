import requests


headers = {
    "Host": "www.zhipin.com",
    "mini_ver": "13.1101",
    "ua": "{\"model\":\"microsoft\",\"platform\":\"windows\"}",
    # "wt2": "EuTetNsahHAu3iJbivjPJAl58gtxUlJuuXq_hdFpHvH80W4CfAhFosEA22mQtF5Zv1QvQpFkvCM8cX3d0FFk_dA~~",
    "zp_app_id": "10002",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/13639",
    "content-type": "application/x-www-form-urlencoded",
    # "traceid": "F-afb5c2lV2LDoCDv4",
    # "mpt": "3d2e233002fd620ede3c3208bd190a33",
    "scene": "1256",
    "xweb_xhr": "1",
    "x-requested-with": "XMLHttpRequest",
    "zp_product_id": "10002",
    "platform": "zhipin/windows",
    "ver": "13.1101",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wxa8da525af05281f3/566/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1, i",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
url = "https://www.zhipin.com/wapi/zpgeek/miniapp/homepage/recjoblist.json"
params = {
    "cityCode": "101250100",
    "sortType": "1",
    "page": "4",
    "pageSize": "15",
    # "encryptExpectId": "6dc6a90fa03b58c40XF80tu_EVFW",
    "districtCode": "",
    "jobType": "2",
    "experience": "108",
    "blueWelfare": "",
    "appId": "10002"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)