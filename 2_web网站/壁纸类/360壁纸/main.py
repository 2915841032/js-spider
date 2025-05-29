import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Origin": "https://huabao.360.cn",
    "Referer": "https://huabao.360.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://app.huabao.360.cn/web/v1/reco/nml"
params = {
    "m2": "",
    "mid": "901600f0200c4fd1a25612201980161e",
    "m": "901600f0200c4fd1a25612201980161e",
    "uid": "901600f0200c4fd1a25612201980161e",
    "v": "0.0.0.0",
    "Bv": "0.0.0.0",
    "FroM": "web",
    "UdU": "901600f0200c4fd1a25612201980161e",
    "oft": "",
    "size": "21",
    "page": "2",
    "c": "1",
    "hsid": "8121014603",
    "num": "6",
    "tid": "0",
    "loc": "1",
    "vip": "0",
    "msize": "0",
    "color": "0",
    "od": "1",
    "rmid": "-1",
    "rmpt": "-1",
    "hb_user_type": "1"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)
