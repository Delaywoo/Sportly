from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Schedule(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300)
    date = models.DateField()
    def __str__(self):
        return self.title #제목을 title 키의 value로. 이 함수는 db를 변경시켜주는 것은 아니라서 migrate 안해줘도 된다.

