import os
import sys
import csv


def load_categories(file_name='categories.csv'):
    from app.models import Category
    total_categories = 0
    total_created_categories = 0
    with open(file_name, encoding='utf-8') as f:
        categories = csv.DictReader(f,)
        for category in categories:
            cat_obj, created = Category.objects.get_or_create(title=category['category'].strip())
            total_categories += 1
            if created:
                total_created_categories += 1
    print('Categories in file', total_categories)
    print('Added new categories', total_created_categories)


def load_products(file_name):
    from app.models import Product, Tag, Category
    product_added = 0
    with open(file_name, encoding='utf-8') as f:
        products = csv.DictReader(f)
        for product in products:
            tags_id = []
            tags_names = product.pop('tags', '').lower().split(',')
            for tag in tags_names:
                tag_obj, crt = Tag.objects.get_or_create(title=tag.strip())
                tags_id.append(tag_obj.pk)
            category = Category.objects.get(title=product.pop('category', '').strip())

            prod, created = Product.objects.get_or_create(
                category=category,
                **product
            )
            prod.tags.add(*tags_id)
            prod.save()
            if created:
                product_added += 1

    print('successful!')
    print('added {} products'.format(product_added))
