# Generated by Django 4.0.4 on 2022-08-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0005_delete_joinpass_join_joinpw'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joinpassword', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]