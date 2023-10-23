from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# class UserProfileForm(forms.Form):
#     password = forms.CharField(widget=forms.PasswordInput(render_value=False), required=False)


class UserRegisterForm(StyleFromMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFromMixin, UserChangeForm):

    submit_button = forms.CharField(label='Сгенерировать новый пароль', widget=forms.widgets.Input(attrs={'type': 'submit', 'value': 'Принять'}), required=False)

    class Meta:
        model = User

        fields = ('email',  'phone', 'country', 'avatar', 'submit_button')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['password'].widget = forms.HiddenInput()


class VerifyForm(StyleFromMixin, forms.Form):
    email_code = forms.IntegerField(max_value=9999)
    error_messages = {
        'required': 'неверный пароль'
    }
    #email = forms.EmailField()
