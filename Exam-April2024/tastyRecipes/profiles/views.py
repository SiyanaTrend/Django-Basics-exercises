from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from common.mixins import SingleObjectMixin
from profiles.forms import ProfileCreateForm
from profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form: ProfileCreateForm):
        if form.is_valid:
            form.save()
            return super().form_valid(form)


class ProfileDetailsView(SingleObjectMixin, DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'

