# Generated by Django 4.2.4 on 2023-10-08 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='дата создания'),
        ),
    ]
