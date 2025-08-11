from django.urls import path, include
from organizer import views

urlpatterns = [
    path('create/', views.CreateOrganizerView.as_view(), name='create-organizer'),
    path('details/', views.OrganizerDetailsView.as_view(), name='organizer-details'),
    path('edit/', views.EditOrganizerView.as_view(), name='edit-organizer'),
    path('delete/', views.DeleteOrganizerView.as_view(), name='delete-organizer'),
]
