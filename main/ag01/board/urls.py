from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('nboard/', views.nboard, name='nboard'),
    path('bwrite/', views.bwrite, name='bwrite'),
]

