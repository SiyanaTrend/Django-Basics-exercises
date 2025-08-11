from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from common.mixins import SingleObjectMixin
from common.utils import get_profile
from events.models import Event
from events.forms import CreateEventForm, EditEventForm, DeleteEventForm


class EventsListView(SingleObjectMixin, ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['-start_time']


class CreateEventView(CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/create-event.html'
    success_url = reverse_lazy('events-list')

    def form_valid(self, form: CreateEventForm):
        form.instance.organizer = get_profile()
        return super().form_valid(form)


class DetailsEventView(DetailView):
    model = Event
    pk_url_kwarg = 'event_pk'
    template_name = 'events/details-event.html'


class EventEditView(UpdateView):
    model = Event
    form_class = EditEventForm
    pk_url_kwarg = 'event_pk'
    template_name = 'events/edit-event.html'

    def get_success_url(self):
        return reverse('event-details', kwargs={'event_pk': self.object.pk})


class DeleteEventView(DeleteView):
    model = Event
    form_class = DeleteEventForm
    template_name = 'events/delete-event.html'
    pk_url_kwarg = 'event_pk'
    success_url = reverse_lazy('events-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    # second solution:

    # def get_form(self, form_class=None):
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #
    #     return form_class(instance=self.get_object())


    # third solution:

    # def get_initial(self) -> dict:
    #     return self.object.__dict__
    #
    # def form_invalid(self, form):
    #     return self.form_valid(form)
