from django.db import models
from django.conf import settings
# 각각의 글들에 해당하는 모델을 만들어 줘야 한다

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null = True, blank = True, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.comment

