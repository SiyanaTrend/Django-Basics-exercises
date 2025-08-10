from django import forms

from common.mixins import ReadOnlyMixin
from recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']

        labels = {
            'title': 'Title:',
            'cuisine_type': 'Cuisine Type:',
            'ingredients': 'Ingredients:',
            'instructions': 'Instructions:',
            'cooking_time': 'Cooking Time',
            'image_url': 'Image URL',
        }


        help_texts = {
            # 'ingredients': 'Ingredients must be separated by a comma and space.',
            'cooking_time': 'Provide the cooking time in minutes.'
        }

        widgets = {
            'ingredients': forms.Textarea(attrs={'placeholder': 'ingredient1, ingredient2, ...'}),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Optional image URL here...'}),
        }

class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(ReadOnlyMixin, RecipeBaseForm):
    read_only_fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
