# 浏览器模式获取动态 token
from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.session_page import SessionPage
page = ChromiumPage()
page.get('https://m.weibo.cn')
# token = page.ele('meta[name="csrf"]').attr('content')

# 切换到 HTTP 模式批量抓取
session = SessionPage()
for page_num in range(2, 6):
    url = f'https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0&since_id={page_num}'
    session.get(url)
    print(session.json['data'])