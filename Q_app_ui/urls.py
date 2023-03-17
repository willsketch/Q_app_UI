"""defines urls for q_app_ui"""
from django.urls import path, include
from . import views

app_name = 'Q_app_ui'
urlpatterns = [
   #Homepage
   path('', views.index, name='index'),
]
