from django.urls import path
from django.contrib.auth.decorators import login_required
from catalog.apps import MainConfig
from catalog.views import contacts, IndexListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    VersionCreateView, VersionUpdateView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index2'),
    path('contacts2/', contacts, name='contacts2'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', login_required(ProductCreateView.as_view()), name='create_product'),
    path('update/<int:pk>/', login_required(ProductUpdateView.as_view()), name='update_product'),
    path('create_v/', login_required(VersionCreateView.as_view()), name='create_version'),
    path('update_v/', login_required(VersionUpdateView.as_view()), name='update_version')
]
