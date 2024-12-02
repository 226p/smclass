from django.urls import path, include
from . import views

app_name = 'foodBoard'
urlpatterns = [
    path('blist/', views.blist, name='blist'),
    path('bview/', views.bview, name='bview'),
]

