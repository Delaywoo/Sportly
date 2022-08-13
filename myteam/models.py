
from datetime import datetime
from importlib.resources import contents
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Tactic(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #writer : User모델에서 username(id) 참조
    #팀 : 외래키로 받아오기
    title = models.TextField()
    date = models.DateField(default=timezone.now) #default=datetime.now(), auto_now_add()
    photo =  models.ImageField(blank=True, null=True, upload_to = 'tactic_photo')
    video = models.FileField(blank=True, null=True, upload_to = 'tactic_file') #파일 업로드 사이즈 최댓값은 기본 2.5mb, 따로 설정 가능.
    contents = models.TextField()
    def __str__(self):
        return self.title


class Notice(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #writer : User모델에서 username(id) 참조
    #팀 : 외래키로 받아오기
    title= models.TextField()
    count = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)
    TAG_CHOICES = (
        ('긴급', '긴급'),
        ('일반', '일반'),
        ('훈련', '훈련'),
    )
    tag= models.TextField( choices = TAG_CHOICES,default='일반')
    contents= models.TextField(null=True)
    photo =  models.ImageField(blank=True, null=True, upload_to = 'notice_photo')
    video = models.FileField(blank=True, null=True, upload_to = 'notice_file') #파일 업로드 사이즈 최댓값은 기본 2.5mb, 따로 설정 가능.
    datetime = models.DateTimeField(default=timezone.now)
    location = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

