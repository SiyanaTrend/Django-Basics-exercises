from django.urls import path, include
from events.views import CreateEventView, EventEditView, DetailsEventView, DetailsEventView, DeleteEventView

urlpatterns = [
    path('create/', CreateEventView.as_view(), name='create-event'),
    path('<int:event_pk>/', include([
        path('edit/', EventEditView.as_view(), name='edit-event'),
        path('details/', DetailsEventView.as_view(), name='event-details'),
        path('delete/', DeleteEventView.as_view(), name='delete-event'),
    ]))
]
