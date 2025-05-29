import requests
import json
import execjs
datacode=open('main.js', 'r', encoding='utf-8').read()
js = execjs.compile(datacode)
uuid = js.call('uuid')


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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    "X-Client-Type": "web",
    "X-Fscp-Bi-Stat": "{\"location\": \"https://www.liepin.com/zhaopin/?inputFrom=head_navigation&scene=init&workYearCode=0&ckId=w16qc9dpc7rc2dz0jskkmr73mqn63d9a\"}",
    "X-Fscp-Fe-Version;": "",
    "X-Fscp-Std-Info": "{\"client_id\": \"40108\"}",
    "X-Fscp-Trace-Id": f"{uuid}",
    "X-Fscp-Version": "1.1",
    "X-Requested-With": "XMLHttpRequest",
    # "X-XSRF-TOKEN": "yEhObrH0St-BTt-fqESJfQ",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

url = "https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job"
data = {
    "data": {
        "mainSearchPcConditionForm": {
            "city": "410",
            "dq": "410",
            "currentPage": 1,
            "pageSize": 100,
            "key": "python",
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
            "otherCity": "",
            "salaryLow": "",
            "salaryHigh": "",
            "hrActiveTimeCode": ""
        },
        "passThroughForm": {
            # "ckId": "74j147m8i7i6pt0kieibkai0p8a3bit9",
            # "skId": "3u7sybmokv0w5nt99sl5930h0dtx78v8",
            # "fkId": "3u7sybmokv0w5nt99sl5930h0dtx78v8",
            "scene": "page",
            "sfrom": "search_job_pc"
        }
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers,  data=data)
print(response.text)
with open('res.json','a', encoding='utf-8') as f:
    f.write(json.dumps(response.json(), ensure_ascii=False, indent=4))