from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from common.mixins import SingleObjectMixin
from common.utils import get_profile
from games.forms import GamesCreateForm, GamesEditForm, GamesDeleteForm
from games.models import Game


class GamesListView(SingleObjectMixin, ListView):
    model = Game
    template_name = 'games/games.html'
    context_object_name = 'games'
    ordering = ['-level', 'title']


class GamesCreateView(CreateView):
    model = Game
    form_class = GamesCreateForm
    template_name = 'games/create-game.html'
    success_url = reverse_lazy('games')

    def form_valid(self, form: GamesCreateForm):
        form.instance.player = get_profile()
        return super().form_valid(form)


class GamesDetailsView(DetailView):
    model = Game
    template_name = 'games/details-game.html'
    pk_url_kwarg = 'game_pk'


class GamesEditView(UpdateView):
    model = Game
    form_class = GamesEditForm
    template_name = 'games/edit-game.html'
    pk_url_kwarg = 'game_pk'

    def get_success_url(self):
        return reverse('game-details', kwargs={'game_pk': self.object.pk})


class GamesDeleteView(DeleteView):
    model = Game
    form_class = GamesDeleteForm
    template_name = 'games/delete-game.html'
    pk_url_kwarg = 'game_pk'
    success_url = reverse_lazy('games')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
