from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
  ## 로그인관련
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
  ## 회원가입 관련 (회원리스트, 회원가입, 회원상세보기, 회원수정)
    path('mlist/', views.mlist, name='mlist'),
    path('mwrite/', views.mwrite, name='mwrite'),
    path('mview/<str:id>/', views.mview, name='mview'),
    path('mupdate/<str:id>/', views.mupdate, name='mupdate'),
    path('mdelete/<str:id>/', views.mdelete, name='mdelete'),
]
