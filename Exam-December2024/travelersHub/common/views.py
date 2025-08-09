from django.shortcuts import render

from common.utils import get_profile
from trips.models import Trip


def index_page_no_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'common/index.html', context)

def traveler_trips(request):
    profile = get_profile()
    trips = Trip.objects.all()

    context = {
        'profile': profile,
        'trips': trips,
    }

    return render(request, 'common/all-trips.html', context)
