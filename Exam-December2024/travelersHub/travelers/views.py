from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from common.utils import get_profile
from travelers.forms import TravelerCreateFrom, TravelerEditForm
from travelers.models import Traveler


class TravelerCreateView(CreateView):
    model = Traveler
    form_class = TravelerCreateFrom
    template_name = 'travelers/create-traveler.html'
    success_url = reverse_lazy('all-trips')

    def form_valid(self, form: TravelerCreateFrom):
        if form.is_valid:
            form.save()
            return super().form_valid(form)

class TravelerDetailView(DetailView):
    model = Traveler
    template_name = 'travelers/details-traveler.html'

    def get_object(self, queryset=None):
        return get_profile()


class TravelerEditView(UpdateView):
    model = Traveler
    form_class = TravelerEditForm
    template_name = 'travelers/edit-traveler.html'
    success_url = reverse_lazy('details-traveler')

    def get_object(self, queryset=None):
        return get_profile()

class TravelerDeleteView(DeleteView):
    model = Traveler
    template_name = 'travelers/delete-traveler.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
