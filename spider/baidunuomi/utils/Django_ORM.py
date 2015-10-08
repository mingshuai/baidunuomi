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
    def SaveZone(self, item):
        zone = Zone()
        zone.zone = item["zone"][0]
        zone.save()

    def SaveCategory(self, item):
        category = Category()
        category.category = item["category"][0]
        category.save()

    def SaveProduct(self, item):
        product = Product()
        product.product_name = item["product"][0]
        product.product_zone = item["zone"][0]
        product.product_category = item["category"][0]
        product.save()

    def SaveProductDetail(self, item):
        product_detail = ProductDetail()
        product_detail.product_name = item["product"][0]
        product_detail.product_price = float(item["product_price"][0])
        if len(item["product_star"]) == 0:
            product_detail.product_star = 0
        else:
            product_detail.product_star = item["product_star"][0]

        product_detail.product_detail = item["product_detail"][0]
        product_detail.product_real_url = item["product_real_url"][0]
        product_detail.save()

    def SaveProductImages(self, item):
        product_image = ProductImages()
        product_image.product_name = item["product"][0]
        product_image.product_real_image_url = item["product_real_image_url"][0]
        product_image.save()


    def SaveItems(self, item):
        self.SaveZone(item)
        self.SaveCategory(item)
        self.SaveProduct(item)
        self.SaveProductDetail(item)
        self.SaveProductImages(item)

    def IsCrawled(self, url):
        try:
            aa = ProductDetail.objects.filter(product_real_url=url)
            if len(aa) != 0:
                return  False
            else:
                return True
        except Exception, e:
            return  True
