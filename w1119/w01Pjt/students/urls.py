from django.urls import path, include
from . import views

app_name = 'students'   # app_name 설정
urlpatterns = [
         # url이름, view호출, name이름
    path('write/', views.write, name='write'),  
    path('search/', views.search, name='search'),  
    path('list/', views.list, name='list'),  
    path('<str:name>/view/', views.view, name='view'),  # view
    path('update/', views.update, name='update'),  # update 파라미터
    # path('<str:name>/update/', views.update, name='update'),  # update app_name
    # path('<str:name>/delete/', views.delete, name='delete'), 
    path('delete/<str:name>/', views.delete, name='delete'), 
]
