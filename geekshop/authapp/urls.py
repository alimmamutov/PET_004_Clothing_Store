

from django.urls import path

from django.conf.urls.static import static

from authapp.views import register, login

# from mainapp.views import products, test
app_name = 'authapp'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]

