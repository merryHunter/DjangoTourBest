# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourbest', '0004_auto_20160102_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='style_id',
            new_name='style',
        ),
    ]
