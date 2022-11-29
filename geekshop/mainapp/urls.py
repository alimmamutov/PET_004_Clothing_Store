

from django.urls import path

from django.conf.urls.static import static

from mainapp.views import products, test
app_name = 'mainapp'
urlpatterns = [
    path('', products, name='products'),
]

