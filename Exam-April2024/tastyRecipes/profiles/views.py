from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from common.mixins import SingleObjectMixin
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form: ProfileCreateForm):
        return super().form_valid(form)


class ProfileDetailsView(SingleObjectMixin, DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'


class ProfileEditView(SingleObjectMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('profile-details')


class ProfileDeleteView(SingleObjectMixin, DeleteView):
    model = Profile
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('home')
