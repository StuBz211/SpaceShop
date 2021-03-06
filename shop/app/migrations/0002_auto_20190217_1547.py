# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-17 10:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sell_price',
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_best_price',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_recommend',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='show_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
