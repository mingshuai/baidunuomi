# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidunuomiItem(scrapy.Item):
    zone = scrapy.Field()
    category = scrapy.Field()
    product = scrapy.Field()
    price = scrapy.Field()
    star = scrapy.Field()
    detail = scrapy.Field()
    real_url = scrapy.Field()
    real_image_url = scrapy.Field()