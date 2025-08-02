from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from albums.models import Album
from common.utils import get_profile


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    success_url = reverse_lazy('home')
    template_name = 'albums/album-add.html'

    def form_valid(self, form: AlbumCreateForm) -> HttpResponseRedirect:
        form.instance.owner = get_profile()
        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'

class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')

    # option 1 - use with def is_valid() - forms.py
    def get_form(self, form_class=None):    # fill the form with data
        form_class = form_class or self.get_form_class()
        return form_class(instance=self.get_object())


    # option 2
    # def get_initial(self) -> dict:   # fill the form with data
    #     return self.object.__dict__
    #
    # def form_invalid(self, form: AlbumDeleteForm):  # no validation of the form, when delete
    #     return self.form_valid(form)

