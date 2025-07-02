# encoding: utf-8
"""
@author: 夏洛
@QQ: 1972386194
@file: 头条测试.py
"""
import urllib3,requests
urllib3.disable_warnings()

def get_sig(url):
    data = {
        "group": "test",
        "action": "tt",
        "url": url
    }
    res = requests.post(url="http://127.0.0.1:5620/business-demo/invoke", data=data, verify=False)
    resp = res.json()
    print(res.json())
    if "?" in url:
        url += "&_signature={}".format(resp['signature'])
    else:
        url += "?_signature={}".format(resp['signature'])
    return url

url = get_sig("https://www.toutiao.com/api/pc/list/feed?channel_id=0&max_behot_time=1698925370&offset=0&category=pc_profile_recommend&aid=24&app_name=toutiao_web")
print(url)
headers = {
    "authority": "www.toutiao.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.toutiao.com/",
    "sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
print(res.text)
# https://www.toutiao.com/api/pc/list/feed?channel_id=0&min_behot_time=1636703275&refresh_count=2&category=pc_profile_recommend&_signature=_02B4Z6wo00d01KWcaZwAAIDAJZ6T3JmB4wiluG0AAEwpfdsN1DmbuNsUZxKy6hQ9zmq5aoV6APEJmbKSJmmYKcV7Mr4VnVYu3tJ11y1TYvRcyhTGsiq5RdbNdsSdf1msDFZUvL.AAJ-zz4GM34