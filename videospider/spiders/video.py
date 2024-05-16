import scrapy
from scrapy import Request

from videospider.items import VideospiderItem


class VideoSpider(scrapy.Spider):
    name = "video"
    allowed_domains = ["hdmoli.pro"]
    start_urls = ["https://www.hdmoli.pro/mlist/index1.html"]

    def parse(self, response, **kwargs):
        main_url = "https://www.hdmoli.pro"
        item = VideospiderItem()
        movie_items = response.xpath('//div[contains(@class,"myui-vodlist__box")]/a')
        for movie in movie_items:
            item['url'] = main_url + movie.xpath('@href').extract_first()
            item['title'] = movie.xpath('@title').extract_first()
            item['score'] = movie.xpath('span[contains(@class,"pic-tag pic-tag-top")]/text()').extract_first()
            yield Request(url=item['url'], method='GET', callback=self.get_movie_info, cb_kwargs=item)
        more_movie = response.xpath('//li[contains(@class,"hidden-xs")]/a/@href').extract()
        for url in more_movie:
            url = main_url + url
            yield Request(url=url, method='GET', callback=self.parse)


    def get_movie_info(self, response, **kwargs):
        item = VideospiderItem(**kwargs)
        print(item)
        movie_info = response.xpath('//ul[contains(@class,"stui-vodlist__text downlist col-pd clearfix")]//p/a')
        data=[]
        for info in movie_info:
            title = info.xpath('@title').extract_first()
            url = info.xpath('@href').extract_first()
            data.append(title+":"+url)
        item['downloadurl'] = data
        yield item

