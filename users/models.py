from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна')
    is_active = models.BooleanField(default=False, verbose_name='активация')
    verif_email_code = models.IntegerField(default=0, verbose_name='код верификации почты')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='дата регистрации')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь' # Настройка для наименования одного объекта
        verbose_name_plural = 'пользователи' # Настройка для наименования набора объектов
        # ordering = ('category_name',)
