from django.urls import path, include
from . import views

app_name = ''   # app_name 설정
urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.index, name='index'),  # home > urls.py 연결
]
