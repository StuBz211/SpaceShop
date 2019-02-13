# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-13 16:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
                ('total_sum', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('order_datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('article', models.CharField(db_index=True, max_length=30, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('price', models.FloatField()),
                ('sell_price', models.FloatField()),
                ('image', models.ImageField(upload_to='web_site/static/images')),
                ('rate', models.FloatField()),
                ('add_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('show_datetime', models.DateTimeField()),
                ('is_new', models.BooleanField()),
                ('is_best_price', models.BooleanField()),
                ('is_recommend', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rate', models.FloatField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('score', models.FloatField(default=0.0)),
                ('privilege_level', models.IntegerField(default=0)),
                ('orders', models.ManyToManyField(related_name='user', to='web_site.Order')),
                ('visited_pages', models.ManyToManyField(related_name='interested', to='web_site.Pages')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed', to='web_site.User'),
        ),
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.ManyToManyField(related_name='product', to='web_site.Review'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='web_site.Tag'),
        ),
        migrations.AddField(
            model_name='pages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='web_site.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.OrderStatus'),
        ),
    ]