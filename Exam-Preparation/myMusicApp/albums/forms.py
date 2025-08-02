from django import forms

from albums.mixins import ReadOnlyMixin
from albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']

        widgets = {
            'album_name': forms.TextInput(
                attrs={'placeholder': 'Album Name'}
            ),
            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description'}
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'Image URL'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Price'}
            ),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass

class AlbumDetailsForm(AlbumBaseForm):
    pass

class AlbumEditForm(AlbumBaseForm):
    pass

class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    # use with option 1 - views.py
    def is_valid(self):  # no validation of the form, when delete
        return True



    # option with fields to choose - see solution 2 - mixins.py
    # read_only_fields = ['album_name', 'artist', 'description']
