import requests


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "priority": "u=1, i",
    "referer": "https://www.nuantang.net/img/%E6%B2%B9%E7%94%BB",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
url = "https://www.nuantang.net/api.php"
params = {
    "cid": "360search",
    "start": "0",
    "count": "10",
    "content": "%E6%B2%B9%E7%94%BB"
}
response = requests.get(url, headers=headers, params=params)

print(response.json())
print(response)
