from datetime import timedelta, datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView, UpdateView
from users.models import User
from users.forms import VerifyForm
from users.forms import UserRegisterForm, UserProfileForm
import random

verif_email_code = random.randint(1000, 9999)


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    #success_url = reverse_lazy('users:profile_active', kwargs={'pk': 1})

    def form_valid(self, form):
        if form.is_valid():

            new_user = form.save(commit=False)
            new_user.verif_email_code = verif_email_code
            new_user.save()
            send_mail(
                subject='Подтверждение почты',
                message=f'Код подтверждения {verif_email_code}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )
            success_url = reverse_lazy('users:profile_active', kwargs={'pk': new_user.id})
            return HttpResponseRedirect(success_url)
        return super().form_valid(form)


def profile_active(request, pk):

    try:
        form = VerifyForm(request.POST)
        new_user = User.objects.get(pk=pk)

        code = new_user.verif_email_code
        time = new_user.created_at + timedelta(minutes=30)
        iso_datetime = time.strftime('%m-%d-%Y %H:%M:%S')
        time_now = datetime.now()
        iso_datetime_now = time_now.strftime('%m-%d-%Y %H:%M:%S')

        if not new_user.is_active:
            if iso_datetime < iso_datetime_now:
                new_user.delete()
                return render(request, 'users/user_404.html')

        if form.is_valid():
            form_data = form.cleaned_data
            active = form_data['email_code']

            if code == active:
                new_user.is_active = True
                new_user.save()

            else:
                form.add_error('email_code', 'Неверный код')

        context = {'user': new_user,
                   'time': iso_datetime,
                   'form': form}

        return render(request, 'users/profile_active.html', context)

    except:
        return render(request, 'users/user_404.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:index2')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):

        if 'submit_button' in form.data:
            new_password = get_random_string(length=6)

            user = self.request.user
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(self.request, user)

            send_mail(
                subject='Обновление данных',
                message=f'Ваш новый пароль {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            messages.success(self.request, f'Новый пароль: {new_password}')

            return self.redirect_to_previous_page()

        return super().form_valid(form)

    def redirect_to_previous_page(self):
        return redirect(self.request.META.get('HTTP_REFERER', '/'))
