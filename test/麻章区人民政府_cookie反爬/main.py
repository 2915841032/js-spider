import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://www.zjmazhang.gov.cn",
    "Pragma": "no-cache",
    "Referer": "http://www.zjmazhang.gov.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "X-CSRF-TOKEN": "E1pQY8frvMCGNiPLLC0MGYr3y0EYx9dhLNZQ8oWJ"
}
cookies = {
    "zh_choose": "n",
    "XSRF-TOKEN": "eyJpdiI6IjBoWTYrNmQrT1Zvdjg0U0xKSFZDZ3c9PSIsInZhbHVlIjoiZ2k3VHZtTUxTanlGNjl3SVFtVUJscGxmb3B2dVpWNmZNNzcyenhPeWRWK09oTHVcL25zXC9Pa1BsRkdcL1Vsb3FURSIsIm1hYyI6Ijg5NWRkNzIyNTE0NmQ2OTg5MDBhNGQyMGZhMDBkMDg3NzdhNTgxYWM2Njk1YmFiZjkxODJmNGQ1MDdkYzY4YjAifQ%3D%3D",
    "szxx_session": "eyJpdiI6IlhGd1ZRMGRSallQZmFHclVHakxsZEE9PSIsInZhbHVlIjoiYzQ2MnNxUlZFbjhYWDhTM3hoSG1NcE5cL2U4amg4N3ZcL241UW12XC9rcThyMHJVcWY3d2x5UzRFdW52YW5VYjBZeSIsIm1hYyI6IjYwY2QxZGJlOTc0YjA1NjVjMTU4Mzg4NDJlOTFkYzJkMjk0ODQ4MTMxMzE1YWYwZWI5MDM1ZDI3MmQ2NGYxNTQifQ%3D%3D"
}
url = "http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList"
data = {
    "offset": "0",
    "limit": "20",
    "site_id": "759010",
    "time_from": "1717862400",
    "time_to": "1749398399"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)

print(response.text)
print(response)