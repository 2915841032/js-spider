"""
Pytho实现同花顺股票数据采集 https://q.10jqka.com.cn/

"""
import requests
import parsel
import csv
import time
import execjs
f = open('data.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '代码',
    '名称',
    '现价',
    '涨跌幅(%)',
    '涨跌',
    '涨速(%)',
    '换手(%)',
    '量比',
    '振幅(%)',
    '成交额',
    '流通股',
    '流通市值',
    '市盈率',
])
# 写入表头
csv_writer.writeheader()

# 模拟浏览器

for i in range(1, 10):
    print(f'---------------------------------------第{i}页-----------------------------------------------------------')
    js_file=open('同花顺.js', encoding='utf-8').read()
    js_code=execjs.compile(js_file)
    v=js_code.eval('zy')
    url = f'https://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{i}/ajax/1/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'Cookie': 'v='+v
    }
    # 发送请求
    response = requests.get(url, headers=header)
    """获取数据: 获取服务器返回响应数据"""
    # 获取响应文本数据
    html = response.text
    """解析数据: 提取我们需要的数据内容"""
    # 把获取到html字符串数据, 转成可解析对象
    selector = parsel.Selector(html)  # <Selector ...'>
    # 提取所有tr标签
    trs = selector.css('.m-table tr')[1:]
    # for循环遍历
    for tr in trs:
        # 提取具体数据内容
        info = tr.css('td::text').getall()  # 提取出来代码 和名称以外的数据
        info_1 = tr.css('td a::text').getall()  # 提取代码和名称
        # 把数据保存到字典里面
        dit = {
            '代码': info_1[0],
            '名称': info_1[1],
            '现价': info[1],
            '涨跌幅(%)': info[2],
            '涨跌': info[3],
            '涨速(%)': info[4],
            '换手(%)': info[5],
            '量比': info[6],
            '振幅(%)': info[7],
            '成交额': info[8],
            '流通股': info[9],
            '流通市值': info[10],
            '市盈率': info[11],
        }
        # 写入数据
        csv_writer.writerow(dit)
        print(dit)

    time.sleep(0.5)