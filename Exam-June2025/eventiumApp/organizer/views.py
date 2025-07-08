from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.utils import timezone

from eventiumApp.utils import get_user_obj
from organizer.forms import CreateOrganizerForm, EditOrganizerForm
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
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        upcoming_events = self.object.events.filter(start_time__gt=timezone.now()).order_by('start_time')
        context['upcoming_events'] = upcoming_events
        return context


class EditOrganizerView(UpdateView):
    model = Organizer
    form_class = EditOrganizerForm
    template_name = 'organizer/edit-organizer.html'
    success_url = reverse_lazy('organizer-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class DeleteOrganizerView(DeleteView):
    model = Organizer
    template_name = 'organizer/delete-organizer.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()

    def post(self, request, *args, **kwargs):
        organizer = self.get_object()
        upcoming_events = organizer.events.filter(start_time__gt=timezone.now())

        if upcoming_events.exists():
            return redirect('index')
        else:
            organizer.events.all().delete()
            organizer.delete()
            return redirect(self.success_url)
