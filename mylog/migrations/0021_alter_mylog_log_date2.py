# Generated by Django 4.0.4 on 2022-08-13 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylog', '0020_alter_mylog_log_date2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylog',
            name='log_date2',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 13, 16, 55, 23, 652734)),
        ),
    ]
