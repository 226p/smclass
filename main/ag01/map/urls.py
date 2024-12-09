from django.urls import path, include
from . import views

app_name = 'map'
urlpatterns = [
    path('mview/', views.mview, name='mview'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('test3/', views.test3, name='test3'),
    path('test4/', views.test4, name='test4'),
    path('test5/', views.test5, name='test5'),
]

