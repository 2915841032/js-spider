import scrapy
from scrapy import cmdline


class DoubanspiderSpider(scrapy.Spider):
    name = "doubanspider"
    allowed_domains = ["movie.douban.com", 'doubanio.com']
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response, **kwargs):
        li_list = response.xpath("//ol[@class='grid_view']/li")
        for li_temp in li_list:
            image_url = li_temp.xpath(".//img/@src").extract_first()
            title = li_temp.xpath(".//span[@class='title'][1]/text()").extract_first()
            rating_num = li_temp.xpath(".//span[@class='rating_num']/text()").extract_first()
            people_num = li_temp.xpath(".//div[@class='star']/span[4]/text()").extract_first()

            yield {
                'type': 'info',
                'image_url': image_url,
                'title': title,
                'rating_num': rating_num,
                'people_num': people_num
            }

            yield scrapy.Request(url=image_url, callback=self.parse_image, cb_kwargs={'image_name': title})

        if response.xpath("//span[@class='next']/a/@href"):
            next_url = response.urljoin(response.xpath("//span[@class='next']/a/@href").extract_first())
            print('开始抓取下一页:', next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            print('全站抓取成功...')

    def parse_image(self, response, image_name):
        yield {
            'type': 'image',
            'image_name': image_name + '.jpg',
            'image_content': response.body
        }


if __name__ == '__main__':
    cmdline.execute('scrapy crawl doubanspider'.split())
