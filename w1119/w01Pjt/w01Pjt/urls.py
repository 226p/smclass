from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자페이지 연결
    path('students/', include('students.urls')),  # students > urls.py 연결
    path('', include('home.urls')),  # home > urls.py 연결
]
