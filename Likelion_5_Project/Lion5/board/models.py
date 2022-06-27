from django.db import models
# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100, null = False)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null = True, blank=True, upload_to = 'board_photo')

    def __str__(self):
        return self.title