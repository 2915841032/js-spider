import requests
import execjs

# 读取 JavaScript 文件内容
with open('1.js', 'r', encoding='utf-8') as file:
    javascript_code = file.read()

# 创建 Context 对象
context = execjs.compile(javascript_code).call('main23')

# 执行 JavaScript 代码
result = context
print(result)
headers = {
    'authority': 'www.ontariogenomics.ca',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'referer': 'https://www.ontariogenomics.ca/news-events/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'cookie': result,
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
}

response = requests.get('https://www.ontariogenomics.ca/news-events/', headers=headers)
print(response.text)


