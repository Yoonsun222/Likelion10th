
from django.conf import settings
from django.contrib import admin
from django.urls import path
from board import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = 'home'),    
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name='create'),    
    path('detail/<int:board_id>', views.detail, name='detail'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)