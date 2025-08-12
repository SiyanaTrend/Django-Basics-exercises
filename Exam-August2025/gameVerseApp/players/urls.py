from django.urls import path

from players import views

urlpatterns = [
    path('', views.PlayerCreateView.as_view(), name='create-player'),
    path('details/', views.PlayerDetailsView.as_view(), name='player-details'),
    path('edit/', views.PlayerEditView.as_view(), name='edit-player'),
    path('delete/', views.PlayerDeleteView.as_view(), name='delete-player'),
]