import requests


headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://zc-paimai.taobao.com",
    "priority": "u=1, i",
    "referer": "https://zc-paimai.taobao.com/",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
}
url = "https://h5api.m.taobao.com/h5/mtop.taobao.datafront.invoke.auctionwalle/1.0/"
params = {
    "jsv": "2.6.1",
    "appKey": "12574478",
    "t": "1740714549319",
    "sign": "41dbcd5d8e9aed92d9f1878b3fcee963",
    "bxPageId": "1410667",
    "api": "mtop.taobao.datafront.invoke.auctionwalle",
    "v": "1.0",
    "type": "originaljson",
    "dataType": "json",
    "requiredParams": "dfApiName,dfUniqueId"
}
data = {
    "data": "{\"dfApp\":\"auctionwalle\",\"dfApiName\":\"auctionwalle.datou.getPageModulesData\",\"dfVariables\":\"{\\\"pageId\\\":1410667,\\\"moduleIds\\\":\\\"9018433170:items\\\",\\\"context\\\":{\\\"_b_9018433170:items\\\":\\\"{\\\\\\\"scm\\\\\\\":\\\\\\\"20140647.julang.pm.sem\\\\\\\",\\\\\\\"a_keywordid\\\\\\\":\\\\\\\"526116059744\\\\\\\",\\\\\\\"bd_vid\\\\\\\":\\\\\\\"10839038816871302087\\\\\\\",\\\\\\\"page\\\\\\\":\\\\\\\"8\\\\\\\",\\\\\\\"userInfo\\\\\\\":{},\\\\\\\"appendMap\\\\\\\":{\\\\\\\"sid\\\\\\\":\\\\\\\"6625213331_1740710050436\\\\\\\"}}\\\",\\\"userInfo\\\":\\\"{}\\\",\\\"device\\\":\\\"pc\\\",\\\"sceneCode\\\":\\\"20200713C5R32B6N\\\"}}\",\"dfUniqueId\":\"1410667.9018433170:items\",\"dfVariablesRecover\":\"{}\"}"
}
response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)