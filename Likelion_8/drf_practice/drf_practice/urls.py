
from email.mime import base
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('practice/', include('practice.urls')),
    path('admin/', admin.site.urls),
   
]


