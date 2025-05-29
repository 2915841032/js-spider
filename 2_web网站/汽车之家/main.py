import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.autohome.com.cn/price/levelid_9/x-x-x-x-3",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "x-nextjs-data": "1"
}

url = "https://www.autohome.com.cn/_next/data/nextweb-prod-c_1.0.159-p_1.46.0/price/levelid_9/x-x-x-x-4.json"
params = {
    "filter": "levelid_9",
    "query": "x-x-x-x-5"
}
response = requests.get(url, headers=headers,  params=params)

print(response.text)
print(response)