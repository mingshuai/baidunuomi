# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidunuomiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZoneItem(scrapy.Item):
    zone = scrapy.Field()

class CategoryItem(scrapy.Item):
    category = scrapy.Field()

class ProductItem(scrapy.Item):
    product = scrapy.Field()
    zone = scrapy.Field()
    category = scrapy.Field()

class ProductDetailItem(scrapy.Item):
    product = scrapy.Field()
    product_price = scrapy.Field()
    product_star = scrapy.Field()
    product_detail = scrapy.Field()
    product_real_url = scrapy.Field()


class ProductImagesItem(scrapy.Item):
    product = scrapy.Field()
    product_real_image_url = scrapy.Field()