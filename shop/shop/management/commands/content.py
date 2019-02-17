import os
import sys


from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        from utils.content_utils import load_categories, load_products
        directory = os.path.join(sys.path[0], 'contents')
        categories_file_path = os.path.join(directory, 'categories.csv')
        product_file_path = os.path.join(directory, 'products.csv')

        load_categories(categories_file_path)
        load_products(product_file_path)
