# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20160915_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='back',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Акционный фон'),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Основное изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название продукта'),
        ),
    ]