from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('blist/', views.blist, name='blist'),   # 게시판
    path('bwrite/', views.bwrite, name='bwrite'),   # 글쓰기
    path('bview/<int:bno>/', views.bview, name='bview'),   # 글 상세보기
]
