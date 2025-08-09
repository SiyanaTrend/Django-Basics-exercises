from django import forms

from common.mixins import ReadOnlyMixin
from trips.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ['traveler']

        labels = {
            'destination': 'Destination:',
            'summary': 'Summary:',
            'start_date': 'Started on:',
            'duration': 'Duration:',
            'image_url': 'Image URL:',
        }

        #  not need, because it is in the model
        # help_texts = {
        #     'duration': '*Duration in days is expected.',
        # }

        widgets = {
            'destination': forms.TextInput(attrs={'placeholder': 'Enter a short destination note...'}),
            'summary': forms.TextInput(attrs={'placeholder': 'Share your exciting moments...'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'An optional image URL...'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TripCreateForm(TripBaseForm):
    pass

class TripEditForm(TripBaseForm):
    pass

class TripDeleteForm(ReadOnlyMixin, TripBaseForm):
    read_only_fields = ['destination', 'image_url', 'summary', 'start_date', 'duration']
