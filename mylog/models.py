from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from colorfield.fields import ColorField

# Create your models here.
class Mylog(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)#writer=...(, 향후 User와 연결시 작성 예정.)
    log_date2=models.DateTimeField(default=timezone.now )
    #mood=models.IntegerField() #각 이모티콘이 1~5의 값을 가짐.
    MOOD_CHOICES = (
        ('😡', '😡'),
        ('😕', '😕'),
        ('😐', '😐'),
        ('🙂', '🙂'),
        ('😜', '😜') 
    )
    mood= models.TextField( choices = MOOD_CHOICES,default='😐')
    learned = models.TextField() #대용량 문자열, 배운 점
    lacked=models.TextField() #부족한점
    improve=models.TextField() #개선할 점
    photo = models.ImageField(blank=True, null=True, upload_to = 'mylog_photo')#비어도 되고, 없어도 된다. 
    video = models.FileField(blank=True, null=True, upload_to = 'mylog_file') #파일 업로드 사이즈 최댓값은 기본 2.5mb, 따로 설정 가능.

    #저장이 media파일 내의 blog_photo에 된다.
    #따로 primary key를 설정해주지 않은 경우, 장고가 알아서 눈에 보이지 않는 id key( value : 1,2,3....)을 만들어
    #primary key로 사용한다.
    #id를 사용하게 될 때는 객체가 만들어진 순서에 따라 숫자가 생기고 그게 primary key가 된다.
    
    #video=models....

    def __str__(self):
        return self.learned #제목을 learned 키의 value로

class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)#writer=...(향후 User와 연결시 작성 예정.)
    comment = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now ) #, auto_now_add = True 
    post = models.ForeignKey(Mylog, on_delete=models.CASCADE)#외래키 블로그 객체 참조
    #on_delete어쩌구는 참조하는 대상이 삭제될 경우 같이 삭제될 것이란 뜻.

    def __str__(self):
        return self.comment #제목을 title 키의 value로. 이 함수는 db를 변경시켜주는 것은 아니라서 migrate 안해줘도 된다.

class Schedule(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300)
    sche_date = models.DateTimeField(default=timezone.now )
    COLOR_CHOICES=(
        ('red','red'),
        ('orange','orange'),
        ('yellow','yellow'),
        ('green','green'),
        ('blue','blue'),
        ('purple','purple')
    )
    color = models.TextField( choices = COLOR_CHOICES,default='red')
    
    
    #color = models.ColorField.(default='#FF0000')
"""
class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)"""