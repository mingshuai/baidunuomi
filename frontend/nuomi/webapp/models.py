# -*- coding: utf-8
from django.db import models
# Create your models here.
class Zone(models.Model):
    zone = models.CharField(max_length=255, verbose_name=u"地区")

class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name=u"分类")

class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name=u"产品名称")
    product_category = models.CharField(max_length=255, verbose_name=u"分类")
    product_zone = models.CharField(max_length=255, verbose_name=u"地区")
     # product_category = models.ForeignKey(Category, related_name='product_category')
     # product_zone = models.ForeignKey(Zone, related_name='product_zone')

class ProductDetail(models.Model):
    product_name = models.CharField(max_length=255, verbose_name=u"产品名称")
    product_price = models.FloatField(max_length=8, verbose_name=u"产品价格")
    product_star = models.CharField(max_length=255, verbose_name=u"产品好评度")
    product_detail = models.CharField(max_length=255, verbose_name=u"产品说明")
    product_real_url = models.CharField(max_length=255, verbose_name=u"产品真实地址")

class ProductImages(models.Model):
    product_name = models.CharField(max_length=255, verbose_name=u"产品名称")
    product_real_image_url = models.CharField(max_length=255, verbose_name=u"产品图片地址")

