from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from common.utils import get_profile
from trips.forms import TripCreateForm
from trips.models import Trip


class TripCreateView(CreateView):
    model = Trip
    form_class = TripCreateForm
    template_name = 'trips/create-trip.html'
    success_url = reverse_lazy('all-trips')

    def form_valid(self, form: TripCreateForm):
        form.instance.traveler = get_profile()
        return super().form_valid(form)


