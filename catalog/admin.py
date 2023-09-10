from django.contrib import admin

from catalog.models import Category, Product

# admin.site.register(Category)
# admin.site.register(Product)
#


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category_name')
    list_filter = ('category_name',)
    search_fields = ('name', 'description')

