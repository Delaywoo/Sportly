# Generated by Django 4.0.4 on 2022-08-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0003_alter_join_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joinpw', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='join',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='jointeam_photo'),
        ),
    ]