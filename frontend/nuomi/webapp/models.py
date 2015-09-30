# -*- coding: utf-8
from django.db import models
# Create your models here.

class zone(models.Model):
    zone = models.CharField(max_length=255, verbose_name=u"地区")

class category(models.Model):
    category = models.CharField(max_length=255, verbose_name=u"分类")

class product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name=u"产品名称")
    # product_category =
    # product_zone =

class product_detail(models.Model):
    # product_id =
    product_price = models.FloatField(max_length=8, verbose_name=u"产品价格")
    product_star = models.FloatField(max_length=3, verbose_name=u"产品好评度")
    product_detail = models.CharField(max_length=255, verbose_name=u"产品说明")
    product_real_url = models.CharField(max_length=255, verbose_name=u"产品真实地址")

class product_images(models.Model):
    product_id = ""
    product_real_image_url = models.CharField(max_length=255, verbose_name=u"产品图片地址")