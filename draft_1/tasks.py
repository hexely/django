from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .models import Settings  # Предположим, что у вас есть модель EmailSchedule


def send_email_task(email, subject, message):
    send_mail(subject, message, 'from@example.com', [email])


def schedule_email_tasks():
    scheduler = BackgroundScheduler()
    scheduler.start()

    # Получите все записи из базы данных
    email_schedules = Settings.objects.all()

    for schedule in email_schedules:
        # Запланируйте выполнение задачи на основе данных из базы данных
        scheduler.add_job(
            send_email_task,
            'interval',
            hours=schedule.frequency_hours,
            args=[schedule.email, schedule.subject, schedule.message],
            start_date=schedule.start_date,
            end_date=schedule.end_date,
            id=str(schedule.id)  # Уникальный идентификатор задачи
        )


# Запустите функцию при запуске приложения Django
schedule_email_tasks()
