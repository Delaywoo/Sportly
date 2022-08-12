# Generated by Django 4.0.6 on 2022-07-28 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylog', '0002_alter_mylog_log_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylog',
            name='log_date2',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 28, 17, 33, 46, 320222)),
        ),
        migrations.AlterField(
            model_name='mylog',
            name='mood',
            field=models.TextField(choices=[('😡', '😡'), ('😠', '😠'), ('😐', '😐'), ('🙂', '🙂'), ('😆', '😆')], default='😐'),
        ),
    ]
