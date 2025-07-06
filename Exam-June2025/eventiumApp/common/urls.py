from django.urls import path
from common.views import IndexPage, EventsListView

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('events/', EventsListView.as_view(), name='events-list')
]