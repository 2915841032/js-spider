from DrissionPage import ChromiumPage

from DrissionPage import ChromiumOptions

# 自动下载并配置 Chromium
# co = ChromiumOptions().auto_install()
co = ChromiumOptions()

# 修改浏览器指纹
co.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

# 禁用 WebRTC
co.set_argument('--disable-webrtc')
# 初始化浏览器（可视化模式）
page = ChromiumPage(addr_or_opts=co)

# 访问目标网站
page.get('https://www.bilibili.com/')

# 定位搜索框并输入关键词
search_box = page.ele('.nav-search-input')
search_box.input('人工智能')

# 点击搜索按钮
search_btn = page.ele('.nav-search-btn')
search_btn.click()

# 智能等待：告别 time.sleep
# 显式等待元素出现（最多10秒）
answer_div = page.wait.ele_loaded('.AnswerItem', timeout=10)
# 等待页面跳转完成
page.wait.load_start()
# 等待 Ajax 加载完成
page.wait.ajax_load('//div[@class="comment-list"]')

