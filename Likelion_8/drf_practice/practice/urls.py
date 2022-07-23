from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.boardlst),
    path('<int:board_id>/', views.board_detail),

]

