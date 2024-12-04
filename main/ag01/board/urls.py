from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('nboard/', views.nboard, name='nboard'),   # 게시판리스트
    path('bwrite/', views.bwrite, name='bwrite'),   # 게시판 글쓰기
    path('gps_test/', views.gps_test, name='gps_test'),   # gps테스트
]

