# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20170319_1503'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='KlingonMovie',
        ),
    ]
