# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 16:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainRest', '0002_auto_20170501_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icon',
            old_name='image_name',
            new_name='name',
        ),
    ]
