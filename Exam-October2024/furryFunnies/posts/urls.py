from django.urls import path, include

from posts import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('<int:post_id>/', include([
        path('details/', views.PostDetailView.as_view(), name='details-post'),
        path('edit/', views.PostEditView.as_view(), name='edit-post'),
        path('delete/', views.PostDeleteView.as_view(), name='delete-post'),
    ])),
]