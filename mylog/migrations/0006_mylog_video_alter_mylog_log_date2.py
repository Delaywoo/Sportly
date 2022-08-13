# Generated by Django 4.0.6 on 2022-07-30 03:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylog', '0005_alter_mylog_log_date2_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylog',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='mylog_file'),
        ),
        migrations.AlterField(
            model_name='mylog',
            name='log_date2',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 30, 12, 55, 28, 193025)),
        ),
    ]
