# Generated by Django 4.0.6 on 2022-08-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('joinpw', models.CharField(max_length=10, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='jointeam_photo')),
            ],
        ),
        migrations.CreateModel(
            name='JoinPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joinpassword', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
