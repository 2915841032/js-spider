
import requests


headers = {
    "Host": "www.zhipin.com",
    "mini_ver": "13.0801",
    "ua": "{\"model\":\"microsoft\",\"platform\":\"windows\"}",
    "zp_app_id": "10002",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/13639",
    "content-type": "application/x-www-form-urlencoded",
    "mpt": "17c70df3677f95696cfeefcf03c5f07e",
    "x-requested-with": "XMLHttpRequest",
    "platform": "zhipin/windows",
    "referer": "https://servicewechat.com/wxa8da525af05281f3/559/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9",
}
url = "https://www.zhipin.com/wapi/zpgeek/miniapp/search/joblist.json"
params = {
    "pageSize": "15",
    "query": "数据分析",
    "city": "101250100",
    "source": "4",
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
    "experience": "102,108",
    "page": "4",
    "appId": "10002"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)
with open('result.json', 'w', encoding='utf-8') as f:
    f.write(response.text)