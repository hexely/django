from django.db import models
from datetime import datetime
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, db_index=True, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов
        ordering = ('category_name',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category_name = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date = models.DateTimeField(default=datetime.now, verbose_name='дата создания')
    date_change = models.DateTimeField(null=True, verbose_name='дата последнего изменения')
    owner_product = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('id',)
        # permission = [
        #     (
        #         "set_published_status",
        #         "Can publish post"
        #     )
        # ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    num_version = models.IntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=50, verbose_name='имя версии')
    is_active = models.BooleanField(default=True, verbose_name='активация')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name_version} {self.product}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('name_version', )
