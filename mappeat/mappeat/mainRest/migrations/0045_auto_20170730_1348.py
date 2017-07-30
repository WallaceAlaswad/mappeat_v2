# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-30 11:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainRest', '0044_auto_20170730_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_detail',
            name='product_name',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateField(db_index=True, default=datetime.date(2017, 7, 30)),
        ),
        migrations.AlterField(
            model_name='ticket_detail',
            name='time',
            field=models.TimeField(default=datetime.time(11, 48, 54, 903344)),
        ),
        migrations.AlterField(
            model_name='ticket_resume',
            name='date',
            field=models.DateField(db_index=True, default=datetime.datetime(2017, 7, 30, 11, 48, 54, 901695, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket_resume',
            name='time',
            field=models.TimeField(db_index=True, default=datetime.time(11, 48, 54, 901768)),
        ),
    ]
