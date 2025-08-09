from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from common.mixins import SingleObjectMixin
from common.utils import get_profile
from trips.models import Trip


class IndexPageNoProfileView(SingleObjectMixin, TemplateView):
    template_name = 'common/index.html'


class TravelerTripsView(SingleObjectMixin, ListView):
    model = Trip
    template_name = 'common/all-trips.html'
    context_object_name = 'trips'
    ordering = ['-start_date']



# def index_page_no_profile(request):
#     profile = get_profile()
#     context = {
#         'profile': profile,
#     }
#     return render(request, 'common/index.html', context)
#
# def traveler_trips(request):
#     profile = get_profile()
#     trips = Trip.objects.all().order_by('-start_date')
#
#     context = {
#         'profile': profile,
#         'trips': trips,
#     }
#
#     return render(request, 'common/all-trips.html', context)