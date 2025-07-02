import requests
import json
import execjs
datacode=open("请求.js","r",encoding="utf-8").read()
ctx = execjs.compile(datacode)
data_ = ctx.call("uuidV4")
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.liepin.com",
    "Pragma": "no-cache",
    "Referer": "https://www.liepin.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "X-Client-Type": "web",
    "X-Fscp-Fe-Version;": "",
    "X-Fscp-Std-Info": "{\"client_id\": \"40108\"}",
    "X-Fscp-Trace-Id": f"{data_}",
    "X-Fscp-Version": "1.1",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job"
data = {
    "data": {
        "mainSearchPcConditionForm": {
            "city": "410",
            "dq": "410",
            "currentPage": 4,
            "pageSize": 100,
            "key": "",
            "suggestTag": "",
            "workYearCode": "0",
            "compId": "",
            "compName": "",
            "compTag": "",
            "industry": "",
            "salaryCode": "",
            "jobKind": "",
            "compScale": "",
            "compKind": "",
            "compStage": "",
            "eduLevel": "",
            "salaryLow": "",
            "salaryHigh": "",
            "hrActiveTimeCode": ""
        },
        # "passThroughForm": {
            # "skId": "tc0aeoepuk6knpwu1xreqh1d6gn6daba",
            # "fkId": "tc0aeoepuk6knpwu1xreqh1d6gn6daba",
            # "scene": "page",
            # "ckId": "qkzvv05jlf6wabc5woj90a96perhjiua",
            # "sfrom": "search_job_pc"
        # }
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers,  data=data)

print(response.text)
print(response)
with open("猎聘3.json","w",encoding="utf-8") as f:
    f.write(json.dumps(response.json(), ensure_ascii=False, indent=4))
