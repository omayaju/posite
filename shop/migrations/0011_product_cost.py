# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20160915_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Стоимость'),
        ),
    ]