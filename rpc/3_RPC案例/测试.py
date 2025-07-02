import requests

data = {
    "group": "rpc-test",
    "action": "ths",
}
res = requests.get("http://127.0.0.1:5620/business-demo/invoke", params=data)
print(res.json())
import requests


headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://q.10jqka.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "hexin-v": "A4PqKjEp76pudKNelKSKRZH6Ekwo-BcIUY1bbrVg3hdYua0yPcinimFc67nG",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "v": f"{res.json()['data']}"
}
url = "https://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/2/ajax/1/"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)