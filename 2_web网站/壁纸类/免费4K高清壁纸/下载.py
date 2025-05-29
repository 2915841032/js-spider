# https://x.haowallpaper.com/link/common/file/getFileImg/15788534234190144.png
import requests
import requests

headers = {
    "Accept": "*/*" ,
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6" ,
    "Connection": "keep-alive" ,
    "Origin": "https://haowallpaper.com" ,
    "Referer": "https://haowallpaper.com/" ,
    "Sec-Fetch-Dest": "empty" ,
    "Sec-Fetch-Mode": "cors" ,
    "Sec-Fetch-Site": "same-site" ,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" ,
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"" ,
    "sec-ch-ua-mobile": "?0" ,
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://x.haowallpaper.com/link/common/file/getFileImg/15788534234190144.png"
params = {
    "data": "m3GO9QmlHTizQSijTWmbJT%2BENgcq3DVaI6h74pfZchVh2qq5kpgQHTr2kITia2MoLYSQAN4x9AS57jIOP3wjCbVhqZvI3eDB4okbOhdkLpp78HRVuglrk2JJvb5F%2Fbf5"
}
response = requests.get(url , headers = headers , )

# print(response.text)
print(response)
with open("壁纸.png" , "wb") as f:
    f.write(response.content)
print("下载完成")
