
import requests

cookies = {
    "__c": "1719830108",
    "wd_guid": "2336f0c9-7d39-4763-b633-1dd324863756",
    "W_CITY_S_V": "15",
    "__g": "-",
    "Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e": "1719830108",
    "historyState": "state",
    "__l": "r=&l=%2Fapi_to%2Fcommon%2Fhead_v2.json%3Fb%3Dachqi-WX0gMGR3dsLlD-u0fzvJ2rY305_BtFkzdTYtIQH6zeSNC8txTlBAkLhgr2Eot6a4lHbFmlsbvj2eiRvw~~%26kiv%3DSotTBW2i0MxwoYmH",
    "__a": "36614770.1719830108..1719830108.3.1.3.3",
    "Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e": "1719830132"
}

headers = {
    'authority': 'www.kanzhun.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': '__c=1692603620; wd_guid=cebfb8df-2411-4ab4-9a09-55b7a0d454ea; __g=-; W_CITY_S_V=15; historyState=state; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1692603622; AB_T=abva; R_SCH_CY_V=5855; __l=r=https%3A%2F%2Fwww.kanzhun.com%2Fsearch%2F%3Fquery%3D%25E8%2585%25BE%25E8%25AE%25AF%26type%3D0&l=%2Fapi_to%2Fcrl%2Fzp_list.json%3Fb%3DiJ85-8opL1_h8RF_EbV-AHJALw9H1aFvM5si5AWxCSrDYj-7UlKRKLbeq1yuZlhbSCiyQVtwEiJQNr4agShknP93qzwJ4PqUzhmo_3RI778~%26kiv%3DUKKYuOvNQrC5uZRu; __a=92758354.1692603620..1692603620.2.1.2.2; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1692603628',
    'href': 'https://www.kanzhun.com/firm/recruit/0nx_3g~~.html?ka=com-recruit-module-expose',
    'pragma': 'no-cache',
    'referer': 'https://www.kanzhun.com/firm/recruit/0nx_3g~~.html?ka=com-recruit-module-expose',
    'reqsource': 'fe',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'x-requested-with': 'XMLHttpRequest',
}



import execjs

# 读取 JavaScript 文件内容
with open('1.js', 'r', encoding='utf-8-sig') as file:
    javascript_code = file.read()

# 创建 Context 对象
kiv,b = execjs.compile(javascript_code).call('main123')

print(b)
print(kiv)


params = {
    'b': b,
    'kiv': kiv,
}


response = requests.get('https://www.kanzhun.com/api_to/crl/zp_list.json', params=params, cookies=cookies, headers=headers)
print(response.text)