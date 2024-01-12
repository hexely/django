from django import forms
from draft_1.models import Settings, Client, Message


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ('date_interval', 'send_time', 'periodicity', 'status',)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
