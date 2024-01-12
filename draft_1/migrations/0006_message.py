# Generated by Django 4.2.4 on 2023-11-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft_1', '0005_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Содержание')),
            ],
        ),
    ]
