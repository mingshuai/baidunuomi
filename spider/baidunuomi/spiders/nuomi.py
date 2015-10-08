# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from baidunuomi.items import BaidunuomiItem
from baidunuomi.utils import Django_ORM



class ExampleSpider(scrapy.Spider):
    name = "nuomi"
    allowed_domains = ["nuomi.com"]
    start_urls = (
        'http://www.nuomi.com/pcindex/main/changecity',
    )
    def parse(self, response):
        sel = Selector(response)
        # 根据选择地区页面,获取到地区和地区的二级页面.并将地区和连接对应起来
        zones = sel.xpath('//ul[@class="cities fl"]/li')
        for index in zones:
            zone_link = index.xpath('a/@href').extract()
            zone_text = index.xpath('a/strong/text()').extract()
            if isinstance(zone_text, list) and len(zone_text) != 0:
               yield Request(url=zone_link[0], callback=self.parse_zone,  meta={'zone':zone_text[0]})

    def parse_zone(self, response):
        # 1. 将地区通过参数传进来
        # 2. 到地区页面去解析分类
        zone = response.meta['zone']
        sel = Selector(response)
        categorys = sel.xpath('//div[@class="level-item"]/div/dl')
        for index in categorys:
            category_link = index.xpath('dt[@class="title"]/a/@href').extract()
            category_text = index.xpath('dt[@class="title"]/a/text()').extract()
            if "nuomi.com" not in category_link[0]:
                pass
            else:
                yield  Request(url=category_link[0], callback=self.parse_category,  meta={'zone':zone, 'category': category_text})

    def parse_category(self, response):
        zone = response.meta['zone']
        category = response.meta['category']
        sel = Selector(response)
        # 获取详细页面连接地址
        pages = sel.xpath('//ul[@class="itemlist clearfix"]/li/a/@href').extract()
        for i in pages:
            if "nuomi.com" not in i:
                pass
            else:
                yield Request(url=i, callback=self.parse_page, meta={'zone':zone, 'category': category})
        # 获取到分页
        page_list = sel.xpath('//div[@class="pager-wrap"]/div[@class="ui-pager"]/a/@href').extract()
        for i in page_list:
            yield Request(url=i, callback=self.parse_category,  meta={'zone':zone, 'category': category})

    def parse_page(self, response):
        sel = Selector(response)
        product_zone = response.meta['zone']
        product_category =  response.meta['category']
        product_name = sel.xpath('//div[@class="w-item-info clearfix"]/h2/text()').extract()
        product_detail = sel.xpath('//div[@class="item-title"]/span/text()').extract()
        product_star = sel.xpath('//div[@class="score fl"]/text()').extract()
        product_price = sel.xpath('//div[@class="match-price-area"]/span[@class="real-price"]/text()').extract()
        #### product_address = sel.xpath('//li[@class="branch branch-open"]/p[@class="branch-address"]/text()').extract() # js解析
        product_images = sel.xpath('//p[@class="wrap-img"]/img/@src').extract()
        crawed = Django_ORM.iscrawled()
        if crawed.IsCrawled(response.url):
            items = []
            item = BaidunuomiItem()
            item["zone"] = [product_zone]
            item["category"] = product_category
            item["product"] = product_name
            item["price"] = product_price
            item["detail"] = product_detail
            item["real_url"] = [response.url]
            item["real_image_url"] = [product_images[0]]
            if len(product_star) != 0:
                item["star"] = product_star
            else:
                item["star"] = [str(product_star)]
            items.append(item)
            return items
        else:
            print response.url + " was crawled! "
            pass





