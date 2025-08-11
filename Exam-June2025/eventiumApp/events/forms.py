from django import forms

from events.mixins import ReadOnlyMixin
from events.models import Event


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer',]

        labels = {
            'slogan': 'Slogan:',
            'location': 'Location:',
            'start_time': 'Event Date/Time:',
            'available_tickets': 'Available Tickets:',
            'key_features': 'Event Key Features:',
            'banner_url': 'Event Banner URL:',
        }

        widgets = {
            'slogan': forms.TextInput(attrs={'placeholder': 'Provide an appealing text...'}),
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'key_features': forms.Textarea(attrs={'placeholder': 'Provide important event details...'}),
            'banner_url': forms.URLInput(attrs={'placeholder': 'An optional banner image URL...'}),
        }


class CreateEventForm(EventBaseForm):
    pass


class EditEventForm(EventBaseForm):
    pass


class DeleteEventForm(ReadOnlyMixin, EventBaseForm):
    read_only_fields = ['slogan', 'location', 'start_time', 'available_tickets', 'key_features', 'banner_url']
