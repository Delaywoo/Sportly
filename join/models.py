from django.db import models
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User 
from myteam.models import Notice, Tactic



# Create your models here.
class Team(models.Model):
    title = models.CharField(max_length=10)
    subtitle=models.CharField(null=True, max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    joinpw = models.CharField(null=True, max_length=10)
    photo = models.ImageField(blank=False, null=False, upload_to = 'jointeam_photo')
    member = models.ManyToManyField(User, related_name='Member',blank=True) #through='JoinPass'
    notices= models.ManyToManyField(Notice, related_name='Notice',blank=True)
    tactics = models.ManyToManyField(Tactic,related_name="Tactic",blank=True)
    def __str__(self):
        return self.title



class JoinPass(models.Model):
    joinpassword = models.CharField(null=True, max_length=10)
    team= models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.team

class RealJoin(models.Model):
    realjoinpw = models.CharField(null=True, max_length=10)

class RealPwd(models.Model):
    realpwd= models.CharField(null=True, max_length=10)

class Check(models.Model):
    real = models.ForeignKey('RealPwd',on_delete=models.CASCADE )
    input = models.CharField(null=True, max_length=10)
