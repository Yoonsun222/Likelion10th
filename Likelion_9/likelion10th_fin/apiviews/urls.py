from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.blog_post_list),
    path('<int:board_id>/', views.blog_detail_post_list),

]

