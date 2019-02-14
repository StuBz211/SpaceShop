from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .mixins import TitleMixin, DescriptionMixin


class Category(TitleMixin):
    """Product category model"""
    pass


class Tag(TitleMixin):
    """Product tag mode"""
    pass


class Review(TitleMixin, DescriptionMixin):
    """product review model"""
    rate = models.FloatField()
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey('User', related_name='reviewed')


class Product(DescriptionMixin):
    """Product model"""
    article = models.CharField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=120)
    price = models.FloatField()
    sell_price = models.FloatField()
    image = models.ImageField(upload_to='web_site/static/images')
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
    """visited page model"""
    url = models.URLField()
    product = models.ForeignKey('Product')


class OrderStatus(TitleMixin):
    """order status model"""
    pass


class Order(models.Model):
    """Order model"""
    number = models.CharField(max_length=50)
    quantity = models.FloatField()
    total_sum = models.FloatField()
    address = models.CharField(max_length=100)
    note = models.TextField()
    status = models.ForeignKey('OrderStatus')
    products = models.ManyToManyField(Product)
    order_datetime = models.DateTimeField(default=datetime.now)


class User(AbstractBaseUser):
    """User model"""

    def get_short_name(self):
        return NotImplemented

    def get_full_name(self):
        return NotImplemented

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=256)
    score = models.FloatField(default=0.0)
    privilege_level = models.IntegerField(default=0)
    visited_pages = models.ManyToManyField(Pages, related_name='interested')
    orders = models.ManyToManyField(Order, related_name='user')
