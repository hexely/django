from django.urls import path
from catalog.apps import MainConfig
from catalog.views import index, contacts, product

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:id>/', product, name='product')
]
