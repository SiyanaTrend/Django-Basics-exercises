from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.utils import timezone

from common.mixins import SingleObjectMixin
from organizer.forms import CreateOrganizerForm, EditOrganizerForm
from organizer.models import Organizer


class CreateOrganizerView(CreateView):
    model = Organizer
    form_class = CreateOrganizerForm
    template_name = 'organizer/create-organizer.html'
    success_url = reverse_lazy('events-list')

    def form_valid(self, form: CreateOrganizerForm):
        return super().form_valid(form)


class OrganizerDetailsView(SingleObjectMixin, DetailView):
    model = Organizer
    template_name = 'organizer/details-organizer.html'
    context_object_name = 'organizer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizer = self.object

        context['upcoming_events'] = (
            organizer.events
            .filter(start_time__gt=timezone.now())
            .order_by('start_time')
        )
        return context


class EditOrganizerView(SingleObjectMixin, UpdateView):
    model = Organizer
    form_class = EditOrganizerForm
    template_name = 'organizer/edit-organizer.html'
    success_url = reverse_lazy('organizer-details')


class DeleteOrganizerView(SingleObjectMixin, DeleteView):
    model = Organizer
    template_name = 'organizer/delete-organizer.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        organizer = self.object
        upcoming_events = organizer.events.filter(start_time__gt=timezone.now())

        if upcoming_events.exists():
            return redirect(self.success_url)

        organizer.events.all().delete()
        organizer.delete()

        return redirect(self.success_url)
