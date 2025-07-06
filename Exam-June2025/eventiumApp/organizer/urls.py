from django.urls import path, include
from organizer.views import CreateOrganizerView, OrganizerDetailsView

urlpatterns = [
    path('create/', CreateOrganizerView.as_view(), name='create-organizer'),
    path('profile/', OrganizerDetailsView.as_view(), name='organizer-details'),
]
