# -*- coding: utf-8
from django.db import models
# Create your models here.


class Zone(models.Model):
    zone = models.CharField(max_length=255, verbose_name=u"地区")

class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name=u"分类")
#    product_zone = models.ForeignKey(Zone, related_name='product_zone')

class Product(models.Model):
     product_name = models.CharField(max_length=255, verbose_name=u"产品名称")
    # aa
     product_category = models.ForeignKey(Category, related_name='product_category')
     product_zone = models.ForeignKey(Zone, related_name='product_zone')


class ProductDetail(models.Model):
#    product_name = models.CharField(max_length=255, verbose_name=u"产品名称")
#    product_category = models.ForeignKey(Category, related_name='product_category')
#    product_zone = models.ForeignKey(Zone, related_name='product_zone')
    product = models.ForeignKey(Product, related_name='product_detail_id')
    product_price = models.FloatField(max_length=8, verbose_name=u"产品价格")
    product_star = models.FloatField(max_length=3, verbose_name=u"产品好评度")
    product_detail = models.CharField(max_length=255, verbose_name=u"产品说明")
    product_real_url = models.CharField(max_length=255, verbose_name=u"产品真实地址")

class ProductImages(models.Model):
    product = models.ForeignKey(ProductDetail, related_name='product_image_id')
    product_real_image_url = models.CharField(max_length=255, verbose_name=u"产品图片地址")