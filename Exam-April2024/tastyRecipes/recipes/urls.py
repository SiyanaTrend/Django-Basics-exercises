from django.urls import path

from recipes import views

urlpatterns = [
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('create/', views.RecipeCreateView.as_view(), name='create-recipe'),

]