from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from authors.forms import AuthorCreateForm, AuthorEditForm
from authors.models import Author
from common.utils import get_profile


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form: AuthorCreateForm):
        if form.is_valid:
            form.save()
            return super().form_valid(form)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_profile()


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_object(self, queryset=None):
        return get_profile()


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
