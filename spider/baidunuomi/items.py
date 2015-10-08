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
    product_price = scrapy.Field()
    product_star = scrapy.Field()
    product_detail = scrapy.Field()
    product_real_url = scrapy.Field()
    product_real_image_url = scrapy.Field()