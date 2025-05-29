import json
import requests
import execjs
jscode=open("create_param.js","r",encoding="utf-8").read()
ctx = execjs.compile(jscode)
t = ctx.call("lank","currency=USD&sort=uawCount&order=desc&range=24h&resultsPerPage=50&page=15&excludedDappId=52142")


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "origin": "https://dappradar.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://dappradar.com/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "x-api-sk": "GqkUXToX7nfGmZVmOsjR86lh42RjcQjZLMi3qNe6pg4"
}
cookies = {
    "non_registered_ga_id": "929d2b6a-cb0c-48e6-8ed3-f84201447b43",
    "cf_clearance": "N6.S9kR9opUSMNN4I.GY9QPtBIfI_4O8KFlyqgQQMnQ-1746716218-1.2.1.1-ZElrFCiJ31qLn1GBq_Yju5pJ8CbgSa0_P.Vni4YYMrBeMPz3hHocNdOxTZJbsOAKVRtVBuCyAaucNINnXmFY_odfNgkdaKVLoy5LOug0gFX16HocOVTFK.Xmt_7B3Wyohs6JiqqpZ0jUxFTeEtrOrf7Zx4g53wpKqcKfHMiI.4wG4W0aOcR5cnq91z4MXlnW2xjmktTxmE0qXtQ98FQCrAvG2umBqSk7IbP2AbDeqF1u_SwFAY.aKHyW8oDxUnQ1CbvoJpNWS91wi1kkzYAgdkFeOJIzrh9SwRYBWJQ3U35QGs04fHYKixSIuU8meXZeX3C0oH.H7_iKzfJv8W.ZtmmZ0oz9lKCRA3asMsYjJxlo58ihbOV6AWzHKliuUeCk",
    "__cf_bm": "T_wZqnEyurOTnZ4N7VJ9wJUdLA2BIG0aFGt8xqqY1oQ-1746716384-1.0.1.1-rPecNmuKvNZd.XmC.PoNbQgaOyETGvmNs0lbn_9BFXX7qRmorTZjVl6TFoJhX1NoLfx1ZQ8rw_OJHp722pig2afK2OGOm1Gx1PVfrnayqN4",
    "dr_session": "{\"sessionId\":\"280ac551-5c8d-417e-b3cb-082df85c5a57\",\"sessionNumber\":1,\"landingPage\":\"/rankings\",\"campaignSource\":\"{\\\"source\\\":null,\\\"medium\\\":null,\\\"campaign\\\":null}\",\"lastActivity\":1746716386636}"
}
url = "https://dapps-rankings.dappradar.com/api/v1.0/rankings/dapps"
params = {
    "params": f"{t}"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)

with open("data1.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(response.json(), ensure_ascii=False, indent=4))
print(response)
