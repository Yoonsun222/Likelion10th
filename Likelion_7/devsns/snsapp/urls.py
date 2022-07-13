from django.contrib import admin
from django.urls import path
from .views import home,postcreate, detail, new_freecomment, new_comment,freehome,freedetail,freepostcreate
urlpatterns = [
    path('', home, name='home' ),
    path('detail/<int:post_id>', detail, name='detail' ),
    path('postcreate/', postcreate, name='postcreate' ),
    path('new_comment/', new_comment, name='new_comment' ),

    path('freehome/', freehome, name='freehome' ),
    path('freedetail/<int:post_id>', freedetail, name='freedetail' ),
    path('freepostcreate/', freepostcreate, name='freepostcreate' ),
    path('new_freecomment/', new_freecomment, name='new_freecomment' ),

]
