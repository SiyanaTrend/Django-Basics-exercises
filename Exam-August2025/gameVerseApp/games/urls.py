from django.urls import path, include

from games import views

urlpatterns = [
    path('', views.GamesListView.as_view(), name='games'),
    path('create/', views.GamesCreateView.as_view(), name='create-game'),
    path('<int:game_pk>/', include([
        path('edit/', views.GamesEditView.as_view(), name='edit-game'),
        path('details/', views.GamesDetailsView.as_view(), name='game-details'),
        path('delete/', views.GamesDeleteView.as_view(), name='delete-game'),
    ])),
]
