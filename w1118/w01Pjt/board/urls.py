from django.urls import path, include
from . import views

app_name = 'board'  # name : url 연결 시 사용
urlpatterns = [
    path('list/', views.list, name='list'),  # 메인페이지 이름 : index, main, default
]
