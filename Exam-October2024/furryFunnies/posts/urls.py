from django.urls import path

from posts import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('<int:post_id>/details/', views.PostDetailView.as_view(), name='details-post'),
    path('<int:post_id>/edit/', views.PostEditView.as_view(), name='edit-post'),
    path('<int:post_id>/delete/', views.PostDeleteView.as_view(), name='delete-post'),
]