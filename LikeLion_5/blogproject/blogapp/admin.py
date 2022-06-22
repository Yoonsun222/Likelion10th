from django.contrib import admin
from .models import Blog


admin.site.register(Blog)
# admin 페이지에서 확인 가능 
# 먼저 admin 계정을 만들어 줘야 함