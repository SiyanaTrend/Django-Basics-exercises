from django.urls import path, include
from organizer.views import CreateOrganizerView, OrganizerDetailsView, EditOrganizerView, DeleteOrganizerView

urlpatterns = [
    path('create/', CreateOrganizerView.as_view(), name='create-organizer'),
    path('details/', OrganizerDetailsView.as_view(), name='organizer-details'),
    path('edit/', EditOrganizerView.as_view(), name='edit-organizer'),
    path('delete/', DeleteOrganizerView.as_view(), name='delete-organizer'),
]
