# Generated by Django 4.0.6 on 2022-08-25 02:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tactic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(upload_to='tactic_photo')),
                ('video', models.FileField(blank=True, null=True, upload_to='tactic_file')),
                ('contents', models.TextField()),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('check_count', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('tag', models.TextField(choices=[('긴급', '긴급'), ('일반', '일반'), ('훈련', '훈련')], default='일반')),
                ('contents', models.TextField(null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='notice_photo')),
                ('video', models.FileField(blank=True, null=True, upload_to='notice_file')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.TextField(blank=True, null=True)),
                ('check_users', models.ManyToManyField(blank=True, related_name='check_notices', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
