import os
import json
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from mainapp.models import Product, ProductCategory

from authapp.models import ShopUser
FILE_PATH = os.path.join(settings.BASE_DIR, 'mainapp/json')


def load_from_json(file_name):
    with open(os.path.join(FILE_PATH, file_name + '.json'), 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    help = 'dont work'

    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)
        
        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            category = ProductCategory.objects.get(name=category_name)
            product['category'] = category
            Product.objects.create(**product)
        
        # ShopUser.objects.create_superuser(username='django', email='', password='geekbrains', age=30)
