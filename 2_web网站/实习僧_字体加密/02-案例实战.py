
import re
import requests
from lxml import etree
from fontTools.ttLib import TTFont



class SXS():
    def __init__(self):
        self.url = 'https://www.shixiseng.com/interns?page={}&type=intern&keyword=%E4%BA%92%E8%81%94%E7%BD%91IT&area&months&days&degree&official&enterprise&salary=-0&publishTime&sortType&city=%E5%85%A8%E5%9B%BD&internExtend'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
        }

    def get_data(self, page):

        res = requests.get(self.url.format(page), headers=self.headers)
        font_url = 'https://www.shixiseng.com' + re.findall('">@font-face {    font-family: myFont;    src: url\((.*?)\);}<', res.text)[0]
        # print(font_url)
        res1 = requests.get(font_url)
        with open('file_sxs.woff', 'wb')as f:
            f.write(res1.content)

        # with open('index.html', 'w', encoding='utf-8')as f:
        #     f.write(res.text)
        return res.text


    def get_font(self):
        font_dict = {}
        font = TTFont('file_sxs.woff')
        for k, v in font.getBestCmap().items():
            # print(k, v)
            if v[3:]:
                content = '\\u00' + v[3:] if len(v[3:]) == 2 else "\\u" + v[3:]
                font_dict[hex(k).replace('0x', '&#x')]  = content.encode('utf-8').decode('unicode_escape')
                # @font-face
        # print(font.getBestCmap())
        return font_dict


    def parse_data(self, font_dict, data):
        # 问题: 传递html 数据  替换不成功    用文本存
        for k,v in font_dict.items():
            data = data.replace(k, v)
        # print(data)
        html_Data = etree.HTML(data)
        div_list = html_Data.xpath('//div[@searchtype="intern"]')
        for div in div_list:
            title = div.xpath('.//div[@class="f-l intern-detail__job"]/p/a/text()')[0]
            price = div.xpath('.//div[@class="f-l intern-detail__job"]/p/span/text()')[0]
            comp = div.xpath('.//div[@class="f-r intern-detail__company"]/p/a[1]/text()')[0]
            print(title, price, comp)


    def main(self):
        for i in range(1, 9):
            data = self.get_data(i)
            font_dict = self.get_font()
            self.parse_data(font_dict, data)


if __name__ == '__main__':
    sxs = SXS()
    sxs.main()











