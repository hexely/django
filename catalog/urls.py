from django.urls import path
from catalog.apps import MainConfig
from catalog.views import contacts, IndexListView, ProductDetailView#, BlogCreateView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),

]
