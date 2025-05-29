import requests
import json


headers = {
    "Host": "newfstj.quyanedu.com",
    "xweb_xhr": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/11581",
    "content-type": "application/json",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wxf3b2751683c2369c/97/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url = "https://newfstj.quyanedu.com/api/index/adjustment_list"
data = {
    "member_id": 521513,
    "page": 1,
    "page_size": 1000,
    "sort_type": "2",
    "start_time": "",
    "end_time": "",
    "word_str": "",
    "province_str": "",
    "major_num": "",
    "major": "",
    "school_type": "",
    "key": "4a87d1c35aafee7d390f57496c3f6552"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

with open("response.json", "w", encoding="utf-8") as f:
    f.write(response.text)
print('数据已保存到response.json')