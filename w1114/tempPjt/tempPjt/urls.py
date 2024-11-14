from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    ### url students들어오면 students>urls.py를 찾아줌
    path('students/',include('students.urls')),
    path('event/',include('event.urls')),
    path('',include('home.urls')),    # 메인화면
]
