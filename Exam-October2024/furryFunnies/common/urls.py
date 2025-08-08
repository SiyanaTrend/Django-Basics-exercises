from django.contrib import admin
from django.urls import path, include
from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]