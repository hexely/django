from django.urls import path
from django.contrib.auth.decorators import login_required
from catalog.apps import MainConfig
from catalog.views import contacts, IndexListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    VersionCreateView, VersionUpdateView, ProductDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index2'),
    path('contacts2/', contacts, name='contacts2'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),  #login_required
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),  #login_required
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'), #login_required
    path('create_v/', VersionCreateView.as_view(), name='create_version'), #login_required
    path('update_v/', VersionUpdateView.as_view(), name='update_version') #login_required
]
