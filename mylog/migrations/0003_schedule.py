# Generated by Django 4.0.6 on 2022-08-13 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mylog', '0002_alter_comment_writer_alter_mylog_writer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('sche_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('color', models.TextField(choices=[('red', 'red'), ('orange', 'orange'), ('yellow', 'yellow'), ('green', 'green'), ('blue', 'blue'), ('purple', 'purple')], default='red')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
