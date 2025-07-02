import scrapy
from scrapy.http import HtmlResponse
from scrapy import cmdline

class QingtingSpider(scrapy.Spider):
    name = "qingting"
    allowed_domains = ["qingting.fm", "pic.qtfm.cn"]
    start_urls = ["https://m.qingting.fm/rank/"]

    def parse(self, response: HtmlResponse, **kwargs):
        data_list = response.css('.item')
        for data in data_list:
            rank = data.css('.badge::text').get()
            title = data.css('.title::text').get()
            desc = data.css('.desc::text').get()
            img_url = data.css('img.cover::attr(src)').get()

            if img_url:  # 确保有图片URL才发起请求
                yield scrapy.Request(
                    img_url,
                    callback=self.parse_image,
                    cb_kwargs={'image_name': title},
                    meta={'rank': rank, 'title': title, 'desc': desc}
                )

            # 同时产出info item
            yield {
                'type': 'info',
                'rank': rank,
                'title': title,
                'desc': desc,
                'img_url': img_url
            }

    def parse_image(self, response: HtmlResponse, image_name):
        # self.logger.info(f'Processing image: {image_name}, status: {response.status}')
        yield {
            'type': 'image',
            'image_name': f"{image_name}.jpg",
            'image_content': response.body,
            'original_url': response.url
        }

if __name__ == '__main__':
    cmdline.execute(['scrapy', 'crawl', 'qingting'])