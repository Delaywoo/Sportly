# Generated by Django 4.0.4 on 2022-08-09 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylog', '0017_alter_mylog_log_date2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylog',
            name='log_date2',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 10, 1, 16, 8, 747676)),
        ),
    ]
