# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 00:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal_Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_meal', models.DateField()),
                ('cost_of_meal', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item_name', models.CharField(max_length=30)),
                ('menu_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Ref_Staff_Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staf_role_description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('staff_role_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Ref_Staff_Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type_table', models.CharField(choices=[('M', 'Mesa'), ('T', 'Terraza'), ('B', 'Barra')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='meals',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Staff'),
        ),
        migrations.AddField(
            model_name='meals',
            name='table_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Table'),
        ),
        migrations.AddField(
            model_name='meal_dishes',
            name='menu_item_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainRest.Menu_Item'),
        ),
    ]
