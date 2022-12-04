from django.shortcuts import render

from authapp.forms import UserLoginForm


# Create your views here.


def login(request):
    context = {
        'title': 'GeekShop | Login',
        'forms': UserLoginForm()
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    context = {
        'title': 'GeekShop | Registration',
    }
    return render(request, 'authapp/register.html', context)
