import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://bulletin.cebpubservice.com/xxfbcmses/search/bulletin.html?searchDate=2000-04-05&dates=300&word=&categoryId=88&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=1&page=4",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "JSESSIONID": "07CE62441CABA27251ACDCB287F64278",
    "Hm_lvt_da6ebc493961b944c4bf10a22517a198": "1743476860",
    "Hm_lpvt_da6ebc493961b944c4bf10a22517a198": "1743476860",
    "HMACCOUNT": "1A29860F78C21A15",
    "acw_tc": "1a0c66d017438497715255625e00357d7e1d482db6dbcf0196b1f4d161d1ed",
    "ssxmod_itna": "YqRO0IqAgGO840dPYIYPCwfx0rrBt0KDGr++u+4GN3G8+DnqD=GFDK40EA8PtRYpKB+e5QLY9Bbw3L0BRc34=YhmRGaaxfe0aDbqGk=KehTeDxpq0rD74irDDxD3Db4QDSDWKD9D04CMnkNgDi3DbxtDf4DmDGYBWqDgDYQDGkKXD7QDIktbDDNbeceDef4eknLYuduM8Ar3ADtDjkTD/RPkoxU3X=Hb/L2Hwc0aWqGytKGu9dNDxdTDCOUDgu0GW7pxWY4GK0jAAAxWYixb87hYKMGRrGq40YAtB7YHKwQdD3sDG+4bjDs4D===",
    "ssxmod_itna2": "YqRO0IqAgGO840dPYIYPCwfx0rrBt0KDGr++w4A=cx3P7D/8DfhK7pt+kph5R75UhwTQtytFm+i3miKLn6IytD6hWvPrCkv9w4c+h5aA+Xfa2=D6iggGxLhLevSnaEDX/uwfN5C18PpIza=AsHcyT6pAF2r9+/6AC2Bew2YoOaSHp6aevNZOatED=H=iYW3POj1TFES3LtgTQj9KKn9ITeidC6rqUfFm80g5L06M0yDyXoNE2NadnIU3CtvIcgD18Hap8BBQtxbMyi5/fHLZ74H6nOy=M4NZS3q=My9l=yqNXxuNC1dNVatahQCCPIoKvomzxeXEfUoI9n=CnE2cXea2mgmUpdAcIQ92p0jt3jitRF63bRN7cL962aSbUiLL7d/orGprBDLifGHgraxxszdvALKCoDrwnje3ewxpI125hGxaDG29GqDRWWDKU4x93N8DFXWk98HV35BDDFqD+r4xD==="
}
url = "https://bulletin.cebpubservice.com/xxfbcmses/search/bulletin.html"
params = {
    "searchDate": "2000-04-05",
    "dates": "300",
    "word": "",
    "categoryId": "88",
    "industryName": "",
    "area": "",
    "status": "",
    "publishMedia": "",
    "sourceInfo": "",
    "showStatus": "1",
    "page": "4",
    # "time__2652": "WqmxyDBQD=itTq05DIYYKu4QqRcjGKD9CoD"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
with open('req.js', 'w', encoding='utf-8') as f:
    f.write(response.text)