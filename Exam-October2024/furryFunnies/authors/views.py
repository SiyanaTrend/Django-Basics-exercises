from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

from authors.forms import AuthorCreateForm
from authors.models import Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form: AuthorCreateForm):
        if form.is_valid:
            form.save()
            return super().form_valid(form)

