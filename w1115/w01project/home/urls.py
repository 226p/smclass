from django.urls import path,include
from . import views

app_name = ''   # app 이름 : 이름으로 접근할 때 사용
urlpatterns = [
  # views.py 연결 - 함수호출
    path('', views.index, name='index'),
]
