from django import forms
from catalog.models import Product, Version
from catalog.services import get_categories_products

RESTRICTED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', "дешево", 'бесплатно', 'обман', 'полиция', 'радар']


class CechMixin:
    def __init__(self, *args, **kwargs):
        # Добавление названий категорий из кеша
        super().__init__(*args, **kwargs)
        categories = get_categories_products()
        self.fields['category_name'].queryset = categories


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StaffProductForm(CechMixin, StyleFromMixin,  forms.ModelForm):
    class Meta:
        model = Product
        fields = ('is_published', 'description', 'category_name')


class ProductForm(StyleFromMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category_name', 'price', 'is_published')
        # exclude = ('is_active')

    def __init__(self, *args, **kwargs):
        # Добавление названий категорий из кеша
        super().__init__(*args, **kwargs)
        categories = get_categories_products()
        self.fields['category_name'].queryset = categories

    def clean_name(self):
        data = self.cleaned_data['name']
        for word in RESTRICTED_WORDS:
            if word in data.lower():
                raise forms.ValidationError('запрещенное слово')
        return data


class VersionForm(StyleFromMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = ('product', 'num_version', 'name_version', 'is_active')
