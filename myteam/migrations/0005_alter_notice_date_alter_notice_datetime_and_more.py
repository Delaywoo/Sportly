# Generated by Django 4.0.6 on 2022-08-11 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myteam', '0004_alter_notice_date_alter_notice_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 8, 11, 16, 18, 8, 985833)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 11, 16, 18, 8, 985833)),
        ),
        migrations.AlterField(
            model_name='tactic',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 8, 11, 16, 18, 8, 985833)),
        ),
    ]