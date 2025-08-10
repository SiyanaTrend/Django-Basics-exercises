from django.urls import path

from profiles import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='create-profile'),
    path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
]