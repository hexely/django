from django import forms
from blog.models import Blog


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFromMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'body', 'preview')
