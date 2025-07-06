from django.urls import path, include
from organizer.views import CreateOrganizerView

urlpatterns = [
    path('create/', CreateOrganizerView.as_view(), name='create-organizer'),
]
