from django.contrib import admin
from draft_1.models import Settings, Client


@admin.register(Settings)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_interval', 'send_time')


@admin.register(Client)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name')

