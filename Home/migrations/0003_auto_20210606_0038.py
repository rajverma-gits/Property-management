# Generated by Django 3.1.5 on 2021-06-05 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 0, 38, 23, 509891)),
        ),
    ]
