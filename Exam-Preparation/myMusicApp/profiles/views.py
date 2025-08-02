from typing import Optional

from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from common.utils import get_profile
from profiles.models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset: Optional[QuerySet]=None) -> QuerySet: # because we have only one profile
        return get_profile()

class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset: Optional[QuerySet]=None) -> QuerySet: # because we have only one profile
        return get_profile()


