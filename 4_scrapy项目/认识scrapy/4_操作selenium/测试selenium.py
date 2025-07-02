import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options

# 创建 Edge 浏览器的选项对象
options = Options()

# 启用无头模式（如果需要）
# options.add_argument("--headless")

# 禁用浏览器的自动化控制条
options.add_argument("--disable-infobars")  # 关闭“自动化控制”提示条
options.add_argument("--disable-extensions")  # 禁用扩展
options.add_argument("--start-maximized")  # 启动时最大化窗口

# 创建 Edge 浏览器实例并应用配置选项

try:
    driver = webdriver.Edge(options=options)
    driver.get("https://www.baidu.com")
    print("Chrome 启动成功！")
    time.sleep(50)
    driver.quit()
except Exception as e:
    print("启动失败，错误信息：", e)
