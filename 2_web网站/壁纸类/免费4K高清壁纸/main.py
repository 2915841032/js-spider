import execjs
import requests
import execjs
function_code=open('请求.js',encoding='utf-8').read()
data_code=execjs.compile(function_code)
plainText = '{"page":"23","sortType":3,"isSel":"true","rows":9,"isFavorites":false,"wpType":1}';

data_file=data_code.call('encrypt',plainText)
print(data_file)



headers = {
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Referer": "https://haowallpaper.com/homeView?isSel=true&page=23",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "accept": "application/json",
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
}
url = "https://haowallpaper.com/link/pc/wallpaper/getWallpaperList"

params = {
    "data": data_file
}
response = requests.get(url, headers=headers, params=params)

data=response.json()['data']


function_code=open('解密.js',encoding='utf-8').read()
data_code=execjs.compile(function_code)
print(data,type(data))
data_file=data_code.call('y',str(data))
print(data_file)