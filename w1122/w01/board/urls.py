from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('blist/', views.blist, name='blist'),    # 게시판리스트
    path('bwrite/', views.bwrite, name='bwrite'),  # 글 쓰기
    path('bview/<str:bno>/', views.bview, name='bview'),  # 글 상세보기
    path('bmodify/<str:bno>/', views.bmodify, name='bmodify'),  # 글 수정하기
    path('bdelete/<str:bno>/', views.bdelete, name='bdelete'),  # 글 삭제하기
    path('breply/<str:bno>/', views.breply, name='breply'),  # 글 답변달기
]
