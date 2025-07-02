import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://htgs.ccgp.gov.cn",
    "Pragma": "no-cache",
    "Referer": "http://htgs.ccgp.gov.cn/GS8/contractpublish/search",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "X-Requested-With": "XMLHttpRequest"
}
cookies = {
    "$HMF_CI": "2d3ba7fc792b273d8b23cff3f70d12befebfa5ea7cfeceb83a894946077d7c38d8afe14d528ae9558121be286f53aa004068a28e64af82d65993af78c5615f351f",
    "JSESSIONIDGS8": "d1eIo6aMN54bBa7vyj1ligfjAIZb10G9Og52K-4Yao2mnneGlcpA\\u0021-64666437",
    "HMY_JC": "4dac3149154c6b105ec979526c90b032a2377e983b503c59ce05ba6a530c00ba26,",
    "HBB_HC": "af47a2a7fc0d0e95b43dcdd177529d7254f08f52a32e2d304996d6c8de6888c31b24239090e43f21ec5660acaec5a5239b",
    "cookieinsert": "20111186"
}
url = "http://htgs.ccgp.gov.cn/GS8/contractpublish/getContractByAjax"
params = {
    "contractSign": "0"
}
data = {
    "searchContractCode": "",
    "searchContractName": "",
    "searchProjCode": "",
    "searchProjName": "",
    "searchPurchaserName": "",
    "searchSupplyName": "",
    "searchAgentName": "",
    "searchPlacardStartDate": "",
    "searchPlacardEndDate": "",
    "code": "pageNoChange",
    "isChange": "",
    "currentPage": "4",
    "codeResult": "cab4f7539db6ec6caaf5d2da7226d3ad"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data, verify=False)

# print(response.text)
# print(response)

with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)