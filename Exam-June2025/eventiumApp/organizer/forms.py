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


        widgets = {
            'company_name': forms.TextInput(
                attrs={'placeholder': 'Enter a company name...'}
            ),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Enter a valid phone number (digits only)...'}
            ),
            'secret_key': forms.PasswordInput(
                attrs={'placeholder': 'Enter a secret key like <1234>...'}
            ),
        }


class CreateOrganizerForm(OrganizerBaseForm):
    class Meta(OrganizerBaseForm.Meta):
        exclude = ['website']


class EditOrganizerForm(OrganizerBaseForm):
    class Meta(OrganizerBaseForm.Meta):
        exclude = ['secret_key']


class DeleteOrganizerForm(OrganizerBaseForm):
    pass
