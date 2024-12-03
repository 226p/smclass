from django.urls import path, include
from . import views

app_name = 'map'
urlpatterns = [
    path('mview/', views.mview, name='mview'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
]

