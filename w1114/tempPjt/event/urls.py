from django.urls import path,include
from . import views    # . 현재라는 뜻 / view에서 모든 페이지를 분배시킴(model에 연결해줌)

app_name = 'event' 
urlpatterns = [
    path('eventView/',views.eventView,name='eventView'),
]
