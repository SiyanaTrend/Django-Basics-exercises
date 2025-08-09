from django.urls import path
from common import views

urlpatterns = [
    path('', views.IndexPageNoProfileView.as_view(), name='index'),
    path('all-trips/', views.TravelerTripsView.as_view(), name='all-trips'),
]

# urlpatterns = [
#     path('', views.index_page_no_profile, name='index'),
#     path('all-trips/', views.traveler_trips, name='all-trips'),
# ]