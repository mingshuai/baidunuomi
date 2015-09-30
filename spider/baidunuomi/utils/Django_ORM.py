__author__ = 'Localhost'
import sys, os

from spider.baidunuomi.settings import path
if path not in sys.path:
    sys.path.append(path)

else Exception, e:
    print  e

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nuomi.settings")
django.setup()


from webapp.models import Zone, Category, Product, ProductDetail, ProductImages


class ProductORM(object):
    def SaveZone(self, item):
        zone = Zone()
        zone.zone = item["zone"]
        zone.save()

    def SaveCategory(self, item):
        category = Category()
        category.category = item["category"]
        category.save()

    def SaveProduct(self, item):
        product = Product()
        product.product_name = item["product"]
        product.product_zone = item["zone"]
        product.product_category = item["category"]
        product.save()

    def SaveProductDetail(self, item):
        product_detail = ProductDetail()
        product_detail.product = item["product"]
        product_detail.product_price = item["product_price"]
        product_detail.product_star = item["product_star"]
        product_detail.product_detail = item["product_detail"]
        product_detail.product_real_url = item["product_real_url"]
        product_detail.save()

    def SaveProductImages(self, item):
        product_image = ProductImages()
        product_image.product = item["product"]
        product_image.product_real_image_url = item["product_real_image_url"]
        product_image.save()
    def IsCrawled(self, url):
        try:
            aa = ProductDetail.objects.filter(product_real_url=url)
            if len(aa) != 0:
                return  False
            else:
                return True
        except Exception, e:
            return  True
