from django.urls import path, include

from trips import views

urlpatterns = [
    path('create/', views.TripCreateView.as_view(), name='create-trip'),
    path('<int:trip_pk>/', include([
        path('details/', views.TripDetailsView.as_view(), name='trip-details'),
        path('edit/', views.TripEditView.as_view(), name='edit-trip'),
        path('delete/', views.TripDeleteView.as_view(), name='delete-trip'),
    ])),
]
