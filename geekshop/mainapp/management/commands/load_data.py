from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Product, ProductCategory
from django.contrib.auth.models import User
from os import path
import json


def load_from_json(file_name):
    parent_dir = path.dirname(path.abspath(__file__))
    with open(path.join(parent_dir, file_name), 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        data = json.load(fh)  # загружаем из файла данные в словарь data
        return data


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        # Creating superuser
        if User.objects.filter(is_superuser=True).count() == 0:
            try:
                User.objects.create_superuser(username='admin', email='', password='1',)
                self.stdout.write("Superuser was created successfully")
            except Exception:
                raise CommandError('Error - Creating superuser')
        else:
            self.stdout.write("Superuser wasn't created because it already exists")

        # filling DB
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()
        categories_dict = load_from_json('../../fixtures/categories.json')
        for category in categories_dict:
            fields = category['fields']
            ProductCategory.objects.create(id=category['pk'], **fields)
        self.stdout.write("Table category was filled successfully")
        products_dict = load_from_json('../../fixtures/products.json')
        for product in products_dict:
            fields = product['fields']
            fields['category'] = ProductCategory.objects.get(id=fields.pop('category'))
            Product.objects.create(id=product['pk'], **fields)
        self.stdout.write("Table products was filled successfully")
