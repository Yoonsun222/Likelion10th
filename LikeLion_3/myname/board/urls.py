from django.contrib import admin
from django.urls import path, include
from board import views
from board.views import first

urlpatterns = [
    path('first/', first)
]