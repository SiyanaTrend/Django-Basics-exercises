from django import forms

from authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'passcode': 'Passcode',
            'pets_number': 'Pets Number',
            'info': 'Info',
            'image_url': 'Profile Image URL'
        }

        # not need, because it is in the model
        # help_texts = {
        #     'passcode': 'Your passcode must be a combination of 6 digits',
        # }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }

class AuthorCreateForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['info', 'image_url']

class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['passcode']
