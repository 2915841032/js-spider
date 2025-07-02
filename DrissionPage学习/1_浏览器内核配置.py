from DrissionPage import ChromiumOptions

# 自动下载并配置 Chromium
co = ChromiumOptions().auto_install()

# 高级配置示例（无头模式 + 中文语言）
co.set_headless(True)
co.set_lang('zh-CN')