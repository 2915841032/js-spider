import requests
import json


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://zjcs.zwfw.gxzf.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://zjcs.zwfw.gxzf.gov.cn/epoint-mhwz-web/page/default/intermediaryServiceGroup",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    # "encrypt": "1",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "JSESSIONID_JAVA": "4E48D508FF32487899E52482949D948C",
    "viewnum": "20006211"
}
url = "https://zjcs.zwfw.gxzf.gov.cn/epoint-mhwz-web/rest/gxindexcontroller/getzjList"
params = {
    "foreSessionClusterIntercept": "true"
}
data = {
    "pageindex": 1,
    "pagesize": 12,
    "order": "Evalution DESC",
    "name": "",
    "taskguid": "",
    "webareacode": ""
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)