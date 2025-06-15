from django.urls import path
from posts.views import index, home_page, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('home/', home_page, name='home'),
    path('dashboard/', dashboard, name='dashboard')
]