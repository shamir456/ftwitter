# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-04-14 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20190414_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='image',
        ),
    ]
