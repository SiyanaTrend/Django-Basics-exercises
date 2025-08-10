from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from common.mixins import SingleObjectMixin
from common.utils import get_profile
from recipes.forms import RecipeCreateForm
from recipes.models import Recipe


class CatalogueView(SingleObjectMixin, ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'
    context_object_name = 'recipes'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form: RecipeCreateForm):
        form.instance.author = get_profile()
        return super().form_valid(form)

class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'recipes/details-recipe.html'
    pk_url_kwarg = 'recipe_id'

