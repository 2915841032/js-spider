import requests
import execjs

cookie = {
    "SUNWAY-ESCM-COOKIE": "18cd31f1-2cc4-495d-a939-db5d1112336b",
    "__jsluid_s": "69efbbb9c8a061490fb4d90efa7518ed",
    "JSESSIONID": "987CD4CB27FD472168752556AE7EA8C3"
}
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'Hm_lvt_f32803886966beff8fa513f7a33dea1e=1692585554; Hm_lpvt_f32803886966beff8fa513f7a33dea1e=1692585587; SUNWAY-ESCM-COOKIE=6ea4d83f-c070-431d-8902-6b6b64457368; __jsluid_s=67b76d4e801e081f216bb5d0844b7e9e; JSESSIONID=EACA322F6285D1584D094593BF2B45CB',
    'Origin': 'https://ec.minmetals.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ec.minmetals.com.cn/open/home/purchase-info',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.post('https://ec.minmetals.com.cn/open/homepage/public', headers=headers,cookies = cookie)
response.encoding='utf-8-sig'
print(response.text)

# 读取 JavaScript 文件内容
with open('2.js', 'r', encoding='utf-8-sig') as file:
    javascript_code = file.read()
# 创建 Context 对象
# param = execjs.compile(javascript_code).call('main123',response.text,1)

# print(param)
print('\n')
json_data = {
    'param':"LobO0x3XZMTOdIUU8OzIeUYHUACimLUg8cW9SD6a+OcT3Zj883/SuAKcAb83M+WJxrgPFfMD8NXJl63eW3i+LEXZc6l7TMRjiLmypnQl/LfiutG6xRB6+HDjMExSTVrbCN0XaJkjXip0L6ELkKBJNUMikCszrxLmEk56VX/48+UQQn9Sxh6fLv/Rqtmmtm+Er8o12hH/Ge7X6NmB6dRFmDzvJjcZKekyIs761so6D5vVKDah0Mrvy+TMIqi5TXejrjvqNMsLxHtdmJJ+1ANPKCR1BD4V4N/+o5AAGH/M6VI48HISOc0XBu27zvtoiC6aRbQMhwlKbX9kArDPJKXuc0AinnL34QxYigI3BiqymPE62r0YBmpNGRo0SkjPsYcdmEkMWy+feoaXXUfVSONJYs6YDMKfO/dzpHPfOYrD/VBBSdrsnu1VX9ZJy8Q6aqIgkcXUfHBQSj7JnSrxV4oZGDoiyK7iE5ublpEtP8tyn6zaNZARu9TifY+0JCh0VxjYNR2HChBJA0CguB5n+Yc+URi4zxcsfzJHlhLxpMhxJZu3yBMhLZL6MagqXxMLyrSmIEb2e1a0WeNpUO6GDfxqlyWgxLi0Gtvoz97giPdc6Gcg3mcInTy16NYShcLI+vxxNGaAzPcNRHVnzFdaiObQpowVU/eGQ++d9KJrpJ6cOPk="
}

response = requests.post('https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',  headers=headers, json=json_data,)
print(response.text)
