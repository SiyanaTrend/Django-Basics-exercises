from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from travelers.forms import TravelerCreateFrom
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

