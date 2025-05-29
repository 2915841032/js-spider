
from curl_cffi import requests

cookies = {
    'gates_cohorts': '%7B%7D',
    '__cf_bm': 'OE2M4o7_bMOZVhvhbUIRpFi7.rpfK25DqjGjRpZpoyQ-1692452561-0-AaCYeDdQPKbATCB6XqpKOAGIxMwxv27k5yNLhkK824jiAsCCbBIHBkRh+SOrjNb34qGJJ9v/xpxo220DvruSO3w=',
}

headers = {
    'authority': 'radar.cloudflare.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'gates_cohorts=%7B%7D; __cf_bm=OE2M4o7_bMOZVhvhbUIRpFi7.rpfK25DqjGjRpZpoyQ-1692452561-0-AaCYeDdQPKbATCB6XqpKOAGIxMwxv27k5yNLhkK824jiAsCCbBIHBkRh+SOrjNb34qGJJ9v/xpxo220DvruSO3w=',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
}

response = requests.get('https://radar.cloudflare.com/traffic/verified-Bots', cookies=cookies, headers=headers,impersonate='edge99')
print(response.text)