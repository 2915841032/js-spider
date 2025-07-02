import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://pan168.cn/resource/detail/4cfaf6815d3948c093449e6d23512287",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "aes": "1057654121",
    "agent": "localhost",
    "fetch": "Yfc5J1elmxTFKxtryzj72w==",
    "md5": "dcbc9a432c995b567b35012c8fd45ef5",
    "random": "1750156548357",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sign": "7460df0bc64b35ff6ba8588962f26545",
    "t-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uX2lkIjoiMTc1MDE1NjU0NDgyMV9yd3dxZ201MXkiLCJ2ZXJpZnlfdmFsdWUiOiJwMXpwcGhja090L3hGbThCOFlaK1hVbXlUNW5sZThRdlh1SjJrU1B1QjVJPSIsImV4cCI6MTc1MDE1NjYwN30.MRnwJUDt--kzHWOuEWvP4xU51iST72wlBvNGmQoRliM"
}
cookies = {
    "clientId": "1057654121",
    "visitorId": "dcbc9a432c995b567b35012c8fd45ef5",
    "session_id": "eyJzZXNzaW9uIjogIjM5ODI5NTMzYTAyM2NlNDFmOTU1YTMxMmIwNzg1NGI0In0=.aFFFAw.aJC2P6n9b1hBISZ70YcZPXa9vjs"
}
url = "https://pan168.cn/web-api/getResourcePanUrl"
params = {
    "source_id": "4cfaf6815d3948c093449e6d23512287"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)