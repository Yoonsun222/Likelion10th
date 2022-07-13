from django.contrib import admin
from django.urls import path
from .views import home,postcreate, detail
urlpatterns = [
    path('', home, name='home' ),
    path('detail/<int:post_id>', detail, name='detail' ),
    path('postcreate/', postcreate, name='postcreate' ),
    path('new_comment/', new_comment, name='new_comment' ),


]
