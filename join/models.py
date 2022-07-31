from django.db import models

# Create your models here.
class Join(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.title