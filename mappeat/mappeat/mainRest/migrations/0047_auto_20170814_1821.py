# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-14 16:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainRest', '0046_auto_20170814_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket_detail',
            old_name='sentKitchen',
            new_name='sent_kitchen',
        ),
        migrations.AlterField(
            model_name='ticket_detail',
            name='time',
            field=models.TimeField(default=datetime.time(16, 21, 14, 443580)),
        ),
        migrations.AlterField(
            model_name='ticket_resume',
            name='time',
            field=models.TimeField(db_index=True, default=datetime.time(16, 21, 14, 442581)),
        ),
    ]