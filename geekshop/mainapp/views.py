from django.shortcuts import render


# Create your views here.
import json
from os import path


def load_from_json(file_name):
    parent_dir = path.dirname(path.abspath(__file__))
    with open(path.join(parent_dir, file_name), 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        data = json.load(fh)  # загружаем из файла данные в словарь data
        return data


def index(request):
    context = {
        'title': 'GeekShop 111',
        'header': 'Welcome to my shop',
        'user': 'Alim',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 200},
            {'name': 'Синяя куртка The North Face', 'price': 300},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 500},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 122},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 250},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 380},
        ],

    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Mamutov Alim\'s Shop' ,
        'header': 'Welcome to my shop',
        'user': 'Alim',
        'products': load_from_json('fixtures/goods.json'),
    }
    return render(request, 'mainapp/products.html', context)


def test(request):
    context = {
        'title': 'GeekShop',
        'header': 'Welcome to my shop',
        'user': 'Alim',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 200},
            {'name': 'Синяя куртка The North Face', 'price': 300},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 500},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 122},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 250},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 380},
        ],

    }
    return render(request, 'mainapp/test_content.html', context)
