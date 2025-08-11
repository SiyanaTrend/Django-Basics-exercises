from django.urls import path, include
from events import views

urlpatterns = [
    path('', views.EventsListView.as_view(), name='events-list'),
    path('create/', views.CreateEventView.as_view(), name='create-event'),
    path('<int:event_pk>/', include([
        path('edit/', views.EventEditView.as_view(), name='edit-event'),
        path('details/', views.DetailsEventView.as_view(), name='event-details'),
        path('delete/', views.DeleteEventView.as_view(), name='delete-event'),
    ]))
]
