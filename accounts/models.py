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