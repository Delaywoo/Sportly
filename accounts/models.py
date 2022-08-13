<<<<<<< HEAD
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
"""
# Create your models here.
class Customuser(AbstractUser):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #username=models.TextField(default="아이디",null = False, blank = False)
    #password=models.TextField(default="비밀번호",null = False, blank = False)
    nickname = models.TextField(default="익명",null = False, blank = False)
    useremail =models.EmailField(default="이메일@naver.com", null = False, blank = False)
    REQUIRED_FIELDS = [nickname,useremail]  # 필수로 받고 싶은 필드들 넣기 
    def __str__(self):
        return self.username #username은 아이디
"""
=======
from django.db import models
from django.contrib.auth.models import AbstractUser

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
>>>>>>> 0896b30a8ed8da04e50de5dafd52929b87d4a1da
