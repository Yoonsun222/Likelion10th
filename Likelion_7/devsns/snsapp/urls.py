from django.contrib import admin
from django.urls import path
from .views import home,postcreate
urlpatterns = [
    path('', home, name='home' ),
    path('postcreate', postcreate, name='postcreate' ),

]
