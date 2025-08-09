from django.urls import path
from common import views

urlpatterns = [
    path('', views.index_page_no_profile, name='index'),
    path('all-trips/', views.traveler_trips, name='all-trips'),
]