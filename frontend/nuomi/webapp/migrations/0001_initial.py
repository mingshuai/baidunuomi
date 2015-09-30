# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, verbose_name='\u5206\u7c7b')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=255, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
            ],
        ),
        migrations.CreateModel(
            name='product_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_price', models.FloatField(max_length=8, verbose_name='\u4ea7\u54c1\u4ef7\u683c')),
                ('product_star', models.FloatField(max_length=3, verbose_name='\u4ea7\u54c1\u597d\u8bc4\u5ea6')),
                ('product_detail', models.CharField(max_length=255, verbose_name='\u4ea7\u54c1\u8bf4\u660e')),
                ('product_real_url', models.CharField(max_length=255, verbose_name='\u4ea7\u54c1\u771f\u5b9e\u5730\u5740')),
            ],
        ),
        migrations.CreateModel(
            name='product_images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_real_image_url', models.CharField(max_length=255, verbose_name='\u4ea7\u54c1\u56fe\u7247\u5730\u5740')),
            ],
        ),
        migrations.CreateModel(
            name='zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zone', models.CharField(max_length=255, verbose_name='\u5730\u533a')),
            ],
        ),
    ]
