from django.db import models
from datetime import datetime
from users.models import User

NULLABLE = {'blank': True, 'null': True}
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='media/', verbose_name='превью', **NULLABLE)
    publ_date = models.DateTimeField(default=datetime.now, verbose_name='дата создания')
    is_valid = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
