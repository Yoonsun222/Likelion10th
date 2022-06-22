from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200) #문자열
    body = models.TextField() #대용량 문자열
    date = models.DateTimeField(auto_now_add=True) #날짜 형식 저장, 자동으로 현재 시간 추가

    def __str__(self):
        return self.title