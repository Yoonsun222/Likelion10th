from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200) #문자열
    body = models.TextField() #대용량 문자열
    date = models.DateTimeField(auto_now_add=True) #날짜 형식 저장, 자동으로 현재 시간 추가
    photo = models.ImageField(blank=True, null = True, upload_to ='blog_photo')


    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True) #날짜 형식 저장, 자동으로 현재 시간 추가
    post = models.ForeignKey(Blog, on_delete = models.CASCADE) #참조 대상 삭제되면 나도 삭제 
     #어떤 게시물에 달려있는 댓글인지 알 수 있는, 댓글에 달린 그 게시물이 쓰임, 블로그 객체를 참조하는 외래키

    def __str__(self):
        return self.comment