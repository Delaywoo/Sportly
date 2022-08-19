# Generated by Django 4.0.6 on 2022-08-20 00:30

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
            name='Mylog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date2', models.DateField(default=django.utils.timezone.now)),
                ('mood', models.TextField(choices=[('😡', '😡'), ('😕', '😕'), ('😐', '😐'), ('🙂', '🙂'), ('😜', '😜')], default='😐')),
                ('learned', models.TextField()),
                ('lacked', models.TextField()),
                ('improve', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='mylog_photo')),
                ('video', models.FileField(blank=True, null=True, upload_to='mylog_file')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylog.mylog')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
