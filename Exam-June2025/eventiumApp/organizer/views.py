from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.utils import timezone

from organizer.forms import CreateOrganizerForm
from organizer.models import Organizer
from events.models import Event

class CreateOrganizerView(CreateView):
    model = Organizer
    form_class = CreateOrganizerForm
    template_name = 'organizer/create-organizer.html'
    success_url = reverse_lazy('events-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

