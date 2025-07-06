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

class OrganizerDetailsView(DetailView):
    model = Organizer
    template_name = 'organizer/details-organizer.html'
    context_object_name = 'organizer'

    def get_object(self, queryset=None):
        return Organizer.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        upcoming_events = self.object.events.filter(start_time__gt=timezone.now()).order_by('start_time')
        context['upcoming_events'] = upcoming_events
        return context