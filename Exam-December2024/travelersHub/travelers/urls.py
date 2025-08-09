from django.urls import path

from travelers import views

urlpatterns = [
    path('create/', views.TravelerCreateView.as_view(), name='create-traveler'),
    # path('details/', views.TravelerDetailView.as_view(), name='details-traveler'),
    # path('edit/', views.TravelerEditView.as_view(), name='edit-traveler'),
    # path('delete/', views.TravelerDeleteView.as_view(), name='delete-traveler'),
]