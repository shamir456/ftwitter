# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-04-14 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
