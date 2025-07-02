import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "origin": "https://www.shixiseng.com",
    "pragma": "no-cache",
    "priority": "u=0",
    "referer": "https://www.shixiseng.com/interns?page=2&type=intern&keyword=&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend=",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "font",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}
cookies = {
    "utm_source_first": "PC",
    "utm_source": "PC",
    "utm_campaign": "PC",
    "position": "pc_default",
    "__jsluid_s": "8f36fa1bd2176254ee0bde7d082f620f"
}
url = "https://www.shixiseng.com/interns/iconfonts/file"
params = {
    "rand": "0.0022665718169340154"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

# print(response.text)
# print(response)
# 写入字体
with open("shixiseng.woff", "wb") as f:
    f.write(response.content)

