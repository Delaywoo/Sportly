from django.db import models
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User 




# Create your models here.
class Team(models.Model):
    title = models.CharField(max_length=10)
    subtitle=models.CharField(null=True, max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    joinpw = models.CharField(null=True, max_length=10)
    photo = models.ImageField(blank=True, null=True, upload_to = 'jointeam_photo')
    member = models.ManyToManyField(User, through='JoinPass', related_name='Member',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title



class JoinPass(models.Model):
    joinpassword = models.CharField(null=True, max_length=10)
    team= models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.team

