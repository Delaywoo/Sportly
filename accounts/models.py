from django.db import models
from django.contrib.auth.models import AbstractUser
"""
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=15, unique=True, verbose_name='username', null=True)
    user_id=models.CharField(max_length=15, unique=True, verbose_name='user_id', null=True)
    password=models.CharField(max_length=30, verbose_name='password', null=True)
    email=models.EmailField(max_length=128, unique=True, verbose_name='email', null=True)
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='signupdate', null=True)
    
    def __str__(self):
        return self.username

    class Meta:
        db_table ='user'
        verbose_name ='유저'
        verbose_name_plural='유저'

"""