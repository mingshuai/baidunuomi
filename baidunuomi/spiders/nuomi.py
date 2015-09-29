# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector




class ExampleSpider(scrapy.Spider):
    name = "nuomi"
    allowed_domains = ["nuomi.com"]
    start_urls = (
        'http://www.nuomi.com/pcindex/main/changecity',
    )

    def parse(self, response):
        sel = Selector(response)
        # 开始选择地区
        zone_link = sel.xpath('//ul[@class="cities fl"]/li/a/@href').extract()
        zone_name = sel.xpath('//ul[@class="cities fl"]/li/a/strong/text()').extract()
        print zone_link

