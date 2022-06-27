from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    #html form을 이용해 블로그 객체를 만들기
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),

    #django form을 이용해 블로그 객체를 만들기    
    path('formcreate/', views.formcreate, name = 'formcreate'),

    #model form을 이용해 블로그 객체를 만들기
    path('modelformcreate/', views.modelformcreate, name = 'modelformcreate'),

    # 127.0.0.1:8000/detail/1
    # 127.0.0.1:8000/detail/2
    # 127.0.0.1:8000/detail/3
    #숫자형으로 설계를 할건데 int형으로 blog_id를 detail함수에 넘겨줄거야
    path('detail/<int:blog_id>', views.detail, name = 'detail'),


]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#mdeail 파일에 접근할 수 있는 url도 추가해 줘야 함
