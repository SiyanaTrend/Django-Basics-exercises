from django import forms

from travelers.models import Traveler


class TravelerBaseForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = '__all__'

        labels = {
            'nickname': 'Nickname:',
            'email': 'Email:',
            'country': 'Country:',
            'about_me': 'About me:'
        }

        # not needed, because it is in the model
        # help_texts = {
        #     'nickname': '*Nicknames can contain only letters and digits.',
        # }

        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': 'Enter a unique nickname...'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter a valid email address...'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter a country code like <BGR>...'}),
        }


class TravelerCreateFrom(TravelerBaseForm):
    class Meta(TravelerBaseForm.Meta):
        exclude = ['about_me']


class TravelerEditForm(TravelerBaseForm):
    pass
