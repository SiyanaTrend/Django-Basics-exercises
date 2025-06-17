from django import forms
from django.core.validators import MinLengthValidator
from posts.models import Post
from posts.validators import BadLanguageValidator
from posts.mixins import ReadOnlyFieldsMixin


class PostBaseForm(forms.ModelForm):
    """example 1"""
    # description = forms.CharField(
    #     validators=[
    #         BadLanguageValidator(),
    #         MinLengthValidator(10, message='The symbols must be at least 10!'),
    #     ]
    # )

    """example 2"""
    # description_text = forms.CharField(
    #     max_length=10,
    #     error_messages={
    #         'max_length': 'The description must be up to 10 symbols!'
    #     }
    # )

    class Meta:
        model = Post
        fields = '__all__'
    widgets = {
        'language': forms.RadioSelect(
            attrs={'class': 'radio-select'},
        )
    }
    error_messages = {
        'author': {
            'max_length': 'The description must be up to 50 symbols!'
        }
    }

    def clean(self):
        pass

class PostCreateForm(PostBaseForm):
    pass

class PostEditForm(PostBaseForm):
    pass

class PostDeleteForm(ReadOnlyFieldsMixin, PostBaseForm):
    pass


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search for posts...'},
        )
    )
