from django.urls import path

from authors import views

urlpatterns = [
    path('create/', views.AuthorCreateView.as_view(), name='create-author'),
    # path('details/', views.AuthorDetailView.as_view(), name='details-author'),
    # path('edit/', views.AuthorUpdateView.as_view(), name='edit-author'),
    # path('delete/', views.AuthorDeleteView.as_view(), name='delete-author'),
]