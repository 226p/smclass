from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    path('write/', views.write, name='write'),  # 학생등록페이지
    path('list/', views.list, name='list'),  # 학생전체리스트
    path('<str:name>/view/', views.view, name='view'),  # 학생정보 상세보기
    path('delete/<str:name>/', views.delete, name='delete'),  # 학생정보 삭제
    path('update/', views.update, name='update'),  # 학생정보 수정
]
