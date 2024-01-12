from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from catalog.apps import MainConfig
from draft_1.views import SettingsCreateView, ClientCreateView

app_name = MainConfig.name

urlpatterns = [
    path('create_set/', SettingsCreateView.as_view(), name='create_settings'),
    path('create_cli/', ClientCreateView.as_view(), name='create_client'),
]
