
from django.contrib import admin
from django.urls import path
from board import views

urlpatterns = [
    path('', views.home, name = 'home'),    
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name='create'),    
    path('admin/', admin.site.urls),
]
