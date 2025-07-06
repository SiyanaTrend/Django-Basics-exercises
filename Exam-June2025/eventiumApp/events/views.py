from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from eventiumApp.utils import get_user_obj
from events.models import Event
from events.forms import CreateEventForm, EditEventForm, DeleteEventForm


class CreateEventView(CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/create-event.html'
    success_url = reverse_lazy('events-list')

    def form_valid(self, form):
        form.instance.organizer = get_user_obj()
        return super().form_valid(form)


class DetailsEventView(DetailView):
    model = Event
    pk_url_kwarg = 'event_pk'
    template_name = 'events/details-event.html'
    context_object_name = 'event'

class EventEditView(UpdateView):
    model = Event
    form_class = EditEventForm
    pk_url_kwarg = 'event_pk'
    template_name = 'events/edit-event.html'
    success_url = reverse_lazy('events-list')


class DeleteEventView(DeleteView):
    model = Event
    form_class = DeleteEventForm
    template_name = 'events/delete-event.html'
    pk_url_kwarg = 'event_pk'
    success_url = reverse_lazy('events-list')

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
