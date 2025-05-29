import requests
import json


headers = {
    "Host": "cgate.zhaopin.com",
    "x-zp-page-code": "7019",
    # "x-zp-rt": "726d8277d6604382bbf1dad27ccb1977",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/11581",
    # "x-zp-device-id": "3DCE8EA2-6D8B-417F-BE93-423240140FC3",
    "content-type": "application/json",
    "x-zp-version": "4.1.161",
    "x-zp-business-system": "73",
    "x-zp-action-id": "",
    "xweb_xhr": "1",
    "x-zp-channel": "wxxiaochengxu",
    "x-zp-platform": "12",
    # "x-zp-at": "0c4d45dd33c748bea7859502820afcd1",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wxb7718fb9257e4fd2/554/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url = "https://cgate.zhaopin.com/positionbusiness/searchrecommend/searchPositions"
data = {
    "eventScenario": "wxmpZhaopinSearchV2",
    "pageIndex": 3,
    "filterMinSalary": 1,
    "S_SOU_EXPAND": "SOU_COMPANY_ID",
    "pageSize": 15,
    "S_SOU_FULL_INDEX": "Python",
    "S_SOU_WORK_CITY": 749,
    "sortType": "DEFAULT"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)
with open('res.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(response.json(), ensure_ascii=False, indent=4))