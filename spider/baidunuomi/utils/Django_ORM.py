# -*- coding: utf-8
__author__ = 'Localhost'
import sys, os

from baidunuomi.settings import path
if path not in sys.path:
    sys.path.append(path)

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nuomi.settings")
django.setup()


from webapp.models import Zone, Category, Product, ProductDetail, ProductImages


class ProductORM(object):
    def SaveProduct(self, item):
        # 保存地区信息
        zone = Zone()
        zone.name = item["zone"][0]
        zone.save()
        # 保存分类信息
        category = Category()
        category.category = item["category"][0]
        category.save()
        # 保存产品信息
        product = Product()
        product.name = item["product"][0]
        product.zone = zone
        product.category = category
        product.save()

        # 保存产品详细信息
        product_detail = ProductDetail()
        product_detail.product = product
        product_detail.price = float(item["price"][0])
        # 这里有问题,需要优化
        try:
            product_detail.price = float(item["price"][0])
            product_detail.star = item["star"][0]
        except Exception, e :
            product_detail.price = float(item["price"])
            product_detail.star = 0
        if product_detail.star == '[]':
            product_detail.star = 0
        product_detail.detail = item["detail"][0]
        product_detail.real_url = item["real_url"][0]
        product_detail.save()

        # 保存产品图片地址信息
        product_image = ProductImages()
        product_image.product = product
        product_image.real_image_url = item["real_image_url"][0]
        product_image.save()

    def SaveItems(self, item):
        self.SaveProduct(item)


class iscrawled(object):

    def IsCrawled(self, url):
        try:
            aa = ProductDetail.objects.filter(product_real_url=url)
            if len(aa) != 0:
                return  False
            else:
                return True
        except Exception, e:
            return  True
