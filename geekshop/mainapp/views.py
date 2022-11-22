from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.tml')


def products(request):
    return render(request, 'products.tml')
