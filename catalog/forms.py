from django import forms
from catalog.models import Product, Version

RESTRICTED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', "дешево", 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFromMixin, forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'image', 'category_name', 'price')
        # exclude = ('is_active')

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
