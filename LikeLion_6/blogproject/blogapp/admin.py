from django.contrib import admin
from .models import Blog, Comment


admin.site.register(Blog)
admin.site.register(Comment)
# admin 페이지에서 확인 가능 
# 먼저 admin 계정을 만들어 줘야 함