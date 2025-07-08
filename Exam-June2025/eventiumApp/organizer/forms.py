from django import forms

from organizer.models import Organizer


class OrganizerBaseForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = '__all__'

        labels = {
            'company_name': 'Company Name:',
            'phone_number': 'Phone Number:',
            'secret_key': 'Secret Key:',
            'website': 'Website:',
        }

        help_texts = {
            'company_name': "*Allowed names contain letters, digits, spaces, and hyphens.",
            'secret_key': "*Pick a combination of 4 unique digits.",
        }

        widgets = {
            'secret_key': forms.PasswordInput(
                attrs={'placeholder': 'Enter a secret key like <1234>...'}
            ),
            'company_name': forms.TextInput(
                attrs={'placeholder': 'Enter a company name...'}
            ),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Enter a valid phone number (digits only)...'}
            ),
        }

class CreateOrganizerForm(OrganizerBaseForm):
    pass

class EditOrganizerForm(OrganizerBaseForm):
    class Meta(OrganizerBaseForm.Meta):
        exclude = ['secret_key']

class DetailsOrganizerForm(OrganizerBaseForm):
    pass


class DeleteOrganizerForm(OrganizerBaseForm):
    pass