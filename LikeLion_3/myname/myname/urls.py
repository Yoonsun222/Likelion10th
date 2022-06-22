from django.contrib import admin
from django.urls import path, include
from leeyoonsun import views
from staticapp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
 
    path('boards/', include('board.urls')),
    path('products/', include('product.urls')),
]
