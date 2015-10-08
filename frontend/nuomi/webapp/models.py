# -*- coding: utf-8
from django.db import models
# Create your models here.
class Zone(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"地区")

class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name=u"分类")

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"产品名称")
    category = models.ForeignKey(Category, related_name='product_category')
    zone = models.ForeignKey(Zone, related_name='product_zone')

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, related_name="product_detail")
    price = models.FloatField(max_length=8, verbose_name=u"产品价格")
    star = models.CharField(max_length=255, verbose_name=u"产品好评度")
    detail = models.CharField(max_length=255, verbose_name=u"产品说明")
    real_url = models.CharField(max_length=255, verbose_name=u"产品真实地址")

class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name="product_image")
    real_image_url = models.CharField(max_length=255, verbose_name=u"产品图片地址")

