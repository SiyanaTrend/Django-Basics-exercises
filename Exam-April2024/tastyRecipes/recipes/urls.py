from django.urls import path, include

from recipes import views

urlpatterns = [
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('create/', views.RecipeCreateView.as_view(), name='create-recipe'),
    path('<int:recipe_id>/', include([
        path('details/', views.RecipeDetailsView.as_view(), name='recipe-details'),
    ])),
]