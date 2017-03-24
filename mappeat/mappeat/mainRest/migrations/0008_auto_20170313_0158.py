# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 01:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainRest', '0007_auto_20170303_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_price', models.FloatField()),
                ('avalible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Mesure_Unity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('simbol', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('price', models.FloatField(default=0)),
                ('icon_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainRest.Icon')),
                ('menu_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Menu_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=90)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('provider_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Provider')),
                ('restaurant_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Supply_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Product')),
            ],
        ),
        migrations.RenameModel(
            old_name='Meal',
            new_name='Ticket_Resume',
        ),
        migrations.RemoveField(
            model_name='meal_dish',
            name='menu_item_ID',
        ),
        migrations.RemoveField(
            model_name='menu_item',
            name='icon_item',
        ),
        migrations.RemoveField(
            model_name='menu_item',
            name='menu_ID',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='icon_ingredient',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='menu_item_ID',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Meal_Dish',
        ),
        migrations.DeleteModel(
            name='Menu_Item',
        ),
        migrations.AddField(
            model_name='ticket_detail',
            name='ticket_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Ticket_Resume'),
        ),
        migrations.AddField(
            model_name='service',
            name='supply_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Supply'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Product'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='restaurant_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Restaurant'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='mesure_unity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainRest.Mesure_Unity'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='product_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainRest.Product'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='supply_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainRest.Supply'),
        ),
    ]