from django import forms

from common.mixins import ReadOnlyMixin
from games.models import Game


class GamesBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ['player']

        labels = {
            'title': 'Title:',
            'platform': 'Platform:',
            'release_date': 'Release Date:',
            'level': 'Challenge Level:',
            'screenshot_url': 'Screenshot URL:',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter games title...'}),
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'screenshot_url': forms.URLInput(attrs={'placeholder': 'Enter screenshot URL...'}),
        }


class GamesCreateForm(GamesBaseForm):
    pass


class GamesEditForm(GamesBaseForm):
    pass


class GamesDeleteForm(ReadOnlyMixin, GamesBaseForm):
    read_only_fields = ['title', 'level', 'screenshot_url']

    class Meta(GamesBaseForm.Meta):
        exclude = ['release_date', 'platform', 'player']
        widgets = {
            'screenshot_url': forms.URLInput(),
        }