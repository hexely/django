from django.db import models
from django.contrib.postgres.fields import DateRangeField


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', **NULLABLE)
    comment = models.TextField(max_length=150, verbose_name='Комментарий', **NULLABLE)


class Settings(models.Model):
    # Выбор статуса рассылки
    STATUS_CHOICES = (
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('finished', 'Завершена'),
    )
    #  Выбор периодичности рассылки
    PERIODICITY_CHOICES = (
        (0, 'один раз'),
        (1, 'раз в день'),
        (7, 'раз в неделю'),
        (30, 'раз в месяц'),
    )

    # Дата начала и окончания рассылки
    date_interval = DateRangeField()
    # start_date = models.DateTimeField()
    # finished_date = models.DateTimeField()
    # Время рассылки
    send_time = models.TimeField()
    # Периодичность рассылки
    periodicity = models.PositiveIntegerField(choices=PERIODICITY_CHOICES)
    # Статус рассылки
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    # Выбор клиентов
    #choise_client = models.


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(verbose_name='Содержание')


# class Log(models.Model):
#     # дата и время последней попытки
#     date_time_last_mailing = models.DateTimeField()
#     # статус попытки
#     status = models.CharField()
#     # ответ почтового сервера, если он был
#     server_response = models.TextField()

