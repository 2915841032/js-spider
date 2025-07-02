import requests
import execjs
datacode=open('模版url的请求data.js',encoding='utf-8-sig').read()
js = execjs.compile(datacode)
token_ = "ack:_1748874819403167438407858758"
P = {
    'wtId': "16671752372997504"
}
G = "https://x.haowallpaper.com/link/common/file/getFileImg"
lank = js.call('lank', token_, P, G)
print(lank)


headers = {
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Origin": "https://haowallpaper.com",
    "Pragma": "no-cache",
    "Referer": "https://haowallpaper.com/homeViewLook/16534772556287360",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "accept": "application/json",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "token": "463F6F52A9073BE4623E18C2BD7C5817"
}
cookies = {
    "askId": "ack%3A_1748874819403167438407858758",
    "downEdit": "true",
    "cropperHint": "ok",
    # "Hm_lvt_3c3619543a455fffe6917f75aba0e02b": "1748904975",
    "isShowElNotice": "ok",
    "isWebsiteLog": "ok",
    "userData": "%7B%22code%22%3A%221930063844311433218%22%2C%22userName%22%3A%22Lank%22%2C%22userImg%22%3A%2217031917911985536%22%2C%22token%22%3A%22463F6F52A9073BE4623E18C2BD7C5817%22%7D"
}
url = "https://haowallpaper.com/link/common/file/getCompleteUrl"
params = {
    "data": f"{lank['res_']}"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params)

# print(response.text)
print(response.status_code)
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(response.text)

res_url=response.json()['data']

res_url = js.call('w', res_url)
import re
res_url = re.sub(r'^[\'"]|[\'"]$', '', str(res_url))
print(res_url)
response = requests.get(res_url, headers=headers, cookies=cookies)
with open('壁纸4.jpg', 'wb') as f:
    f.write(response.content)
print('下载完成')
