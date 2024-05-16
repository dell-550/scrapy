# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VideospiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    score = scrapy.Field()
    url = scrapy.Field()
    downloadurl = scrapy.Field()
    # movietype = scrapy.Field()

