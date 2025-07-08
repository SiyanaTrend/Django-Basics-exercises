from django import forms
from django.utils import timezone

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
            'slogan': forms.TextInput(attrs={
                'placeholder': 'Provide an appealing text...'
            }),
            'location': forms.TextInput(),
            'start_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
            }),
            'available_tickets': forms.NumberInput(),
            'key_features': forms.Textarea(attrs={
                'placeholder': 'Provide important event details...',
                'rows': 4,
            }),
            'banner_url': forms.URLInput(attrs={
                'placeholder': 'An optional banner image URL...'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            self.fields['start_time'].initial = timezone.now().strftime('%Y-%m-%dT%H:%M')


class CreateEventForm(EventBaseForm):
    pass

class EditEventForm(EventBaseForm):
    def clean_banner_url(self):
        data = self.cleaned_data.get('banner_url')
        if not data:
            return self.instance.banner_url
        return data

class DetailsEventForm(EventBaseForm):
    pass

class DeleteEventForm(ReadOnlyMixin, EventBaseForm):
    read_only_fields = ['slogan', 'location', 'start_time', 'available_tickets', 'key_features', 'banner_url']
