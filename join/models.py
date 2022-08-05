from django.db import models
from django.conf import settings

# Create your models here.
class Join(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    #post = 어떤 게시물에 달려있는 댓글인지를 알 수 있는 댓글이 달린 그 게시물이 쓰임
    post = models.ForeignKey(Join, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment