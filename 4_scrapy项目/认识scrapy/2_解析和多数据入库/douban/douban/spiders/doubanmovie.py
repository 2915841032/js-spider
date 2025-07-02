import scrapy
import scrapy.cmdline


class DoubanmovieSpider(scrapy.Spider):
    name = "doubanmovie"
    allowed_domains = ["douban.com", 'doubanio.com','*']
    start_urls = ["https://movie.douban.com/top250"]

    # 在写入数据库前,去除数据库不能写入的字符
    def clean_text(self,text):
        if text:
            text=text.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
            return text
        else:
            return ''



    def parse(self, response):
        data=response.css('.item')
        for item in data:
            title=item.css('.title::text').get()
            rate=item.css('.rating_num::text').get()
            rate_number=item.css('div.bd div span:last-child::text').get()
            img_url=item.css('.pic img::attr(src)').get()
            desc=item.css('.bd p::text').get()

            # 对字段进行处理
            title=self.clean_text(title)
            rate=self.clean_text(rate)
            rate_number=self.clean_text(rate_number)
            img_url=self.clean_text(img_url)
            desc=self.clean_text(desc)

            yield scrapy.Request(img_url,callback=self.parse_img, meta={'title':title, 'rate':rate, 'rate_number':rate_number, 'desc':desc,'img_url':img_url})
    #     翻页
        next_page=response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
    def parse_img(self, response):
        title=response.meta['title']
        rate=response.meta['rate']
        rate_number=response.meta['rate_number']
        desc=response.meta['desc']
        img_url=response.meta['img_url']
        img=response.body
        yield {
            'title':title,
            'rate':rate,
            'rate_number':rate_number,
            'desc':desc,
            'img':img,
            'img_url':img_url
        }



if __name__ == '__main__':
    scrapy.cmdline.execute(['scrapy', 'crawl', 'doubanmovie'])
