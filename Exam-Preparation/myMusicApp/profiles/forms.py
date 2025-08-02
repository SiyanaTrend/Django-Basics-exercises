from django import forms

from albums.mixins import PlaceholderMixin
from profiles.models import Profile


class ProfileBaseForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


        # Using PlaceholderMixin instead of:

        # widgets = {
        #     'username': forms.TextInput(
        #         attrs={'placeholder': 'Username'}
        #     ),
        #     'email': forms.EmailInput(
        #         attrs={'placeholder': 'Email'}
        #     ),
        #     'age': forms.NumberInput(
        #         attrs={'placeholder': 'Age'}
        #     ),
        # }


class ProfileCreateForm(ProfileBaseForm):
    pass
