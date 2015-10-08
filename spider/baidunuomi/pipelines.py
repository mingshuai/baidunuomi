# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from utils import Django_ORM

class BaidunuomiPipeline(ImagesPipeline):
    # 从item中获取图片的真实地址，并执行下载请求
    def get_media_requests(self, item, info):
        for image_url in item['real_image_url']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [[x['path'] for ok, x in results if ok]]
        if not image_paths:
            raise DropItem("Item contains no images")

        print "========================================"
        print u"产品地区:" + item["zone"][0]
        print u"产品分类:" + item["category"][0]
        print u"产品名称:" + item["product"][0]
        print u"产品说明:" + item["detail"][0]
        print  u"产品星级:" + item["star"][0]
        print u"产品价格:" + item["price"][0]
        print u"产品图片地址:" + item["real_image_url"][0]
        print u"产品实际地址:" + item["real_url"][0]
        save_Data = Django_ORM.ProductORM()
        save_Data.SaveItems(item)
        return

    def file_path(self, request, response=None, info=None):
        url = request.url
        image_guid = url.split('/')[-1]
        return '%s.jpg' % (image_guid)