from django.urls import path

from common import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
]
