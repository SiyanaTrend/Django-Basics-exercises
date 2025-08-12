from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from common.mixins import SingleObjectMixin
from players.forms import PlayerCreateForm, PlayerEditForm
from players.models import Player


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerCreateForm
    template_name = 'players/create-player.html'
    success_url = reverse_lazy('games')

    def form_valid(self, form: PlayerCreateForm):
        return super().form_valid(form)


class PlayerDetailsView(SingleObjectMixin, DetailView):
    model = Player
    template_name = 'players/details-player.html'
    context_object_name = 'player'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['top_games'] = self.object.games.order_by('-level', 'title')[:3]

        return context


class PlayerEditView(SingleObjectMixin, UpdateView):
    model = Player
    form_class = PlayerEditForm
    template_name = 'players/edit-player.html'
    success_url = reverse_lazy('player-details')


class PlayerDeleteView(SingleObjectMixin, DeleteView):
    model = Player
    template_name = 'players/delete-player.html'
    success_url = reverse_lazy('index')
