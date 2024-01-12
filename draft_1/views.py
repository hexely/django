from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from draft_1.forms import SettingsForm, ClientForm, MessageForm
from draft_1.models import Settings, Client, Message
from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler
from .test import print_hello_world

scheduler = BackgroundScheduler()
scheduler.add_job(print_hello_world, 'interval', seconds=5,  id='test', name='test')
scheduler.start()


class SettingsCreateView(CreateView):
    model = Settings
    form_class = SettingsForm
    model_2 = Message
    form_class_2 = MessageForm
    permission_required = 'draft_1.add_settings'
    # a = Settings.objects.get(pk=1)
    # print(a.date_interval)
    # print(a.date_interval.lower)
    # print(a.date_interval.upper)
    success_url = reverse_lazy('catalog:index2')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_2'] = self.form_class_2()
        return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    permission_required = 'draft_1.add_client'
    success_url = reverse_lazy('catalog:index2')

