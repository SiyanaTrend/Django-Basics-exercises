from django.urls import path
from common.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
]
