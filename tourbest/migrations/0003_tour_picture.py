# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourbest', '0002_auto_20160101_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
