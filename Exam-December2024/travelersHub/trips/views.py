from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from common.utils import get_profile
from trips.forms import TripCreateForm, TripEditForm, TripDeleteForm
from trips.models import Trip


class TripCreateView(CreateView):
    model = Trip
    form_class = TripCreateForm
    template_name = 'trips/create-trip.html'
    success_url = reverse_lazy('all-trips')

    def form_valid(self, form: TripCreateForm):
        form.instance.traveler = get_profile()
        return super().form_valid(form)


class TripDetailsView(DetailView):
    model = Trip
    pk_url_kwarg = 'trip_pk'
    template_name = 'trips/details-trip.html'


class TripEditView(UpdateView):
    model = Trip
    form_class = TripEditForm
    pk_url_kwarg = 'trip_pk'
    template_name = 'trips/edit-trip.html'
    success_url = reverse_lazy('all-trips')

class TripDeleteView(DeleteView):
    model = Trip
    form_class = TripDeleteForm
    pk_url_kwarg = 'trip_pk'
    template_name = 'trips/delete-trip.html'
    success_url = reverse_lazy('all-trips')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
