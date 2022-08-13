from django.db import models
from django.conf import settings

# Create your models here.
class Join(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.title
=======
    title = models.CharField(max_length=10)
    subtitle=models.CharField(null=True, max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    joinpw = models.CharField(null=True, max_length=10)
    photo = models.ImageField(blank=True, null=True, upload_to = 'jointeam_photo')
    
    def __str__(self):
        return self.title

class JoinPass(models.Model):
    joinpassword = models.CharField(null=True, max_length=10)
>>>>>>> 0896b30a8ed8da04e50de5dafd52929b87d4a1da
