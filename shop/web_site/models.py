from datetime import datetime

from django.db import models


# todo add class to mixins.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.FloatField()
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey('User', related_name='reviewed')


class Tag(models.Model):
    name = models.CharField(max_length=256)


class Product(models.Model):
    article = models.CharField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField()
    sell_price = models.FloatField()
    # image = models.ImageField(upload_to='web_site/static/images')  # todo install pillow
    category = models.ForeignKey('Category', db_index=True)
    tags = models.ManyToManyField(Tag, related_name='products')
    reviews = models.ManyToManyField(Review, related_name='product')
    rate = models.FloatField()
    add_datetime = models.DateTimeField(default=datetime.now)
    show_datetime = models.DateTimeField()
    is_new = models.BooleanField()
    is_best_price = models.BooleanField()
    is_recommend = models.BooleanField()


class Pages(models.Model):
    url = models.URLField()
    product = models.ForeignKey('Product')


class OrderStatus(models.Model):
    name = models.CharField(max_length=50)


class Order(models.Model):
    number = models.CharField(max_length=50)
    quantity = models.FloatField()
    total_sum = models.FloatField()
    address = models.CharField(max_length=100)
    note = models.TextField()
    status = models.ForeignKey('OrderStatus')
    products = models.ManyToManyField(Product)
    order_datetime = models.DateTimeField(default=datetime.now)


class User(models.Model):
    login = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=50)
    score = models.FloatField(default=0.0)
    privilege_level = models.IntegerField(default=0)
    visited_pages = models.ManyToManyField(Pages, related_name='interested')
    orders = models.ManyToManyField(Order, related_name='user')
