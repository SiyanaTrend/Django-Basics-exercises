from crispy_forms.helper import FormHelper
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.forms import modelformset_factory, formset_factory

from posts.models import Post, Comment
from posts.validators import BadLanguageValidator
from posts.mixins import ReadOnlyFieldsMixin


class PostBaseForm(forms.ModelForm):
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
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title.lower() in content.lower():
            raise ValidationError('The post title should not be included in the content!')

        return cleaned_data

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if not author.isalpha():
            raise ValidationError('Author name should contain only letters')

        return author

    def save(self, commit=True):
        """commit=False => create the instance, but not in the database"""
        post = super().save(commit=False)

        post.author = post.author.capitalize()

        """save the post with author's name with capitalize() in database"""
        if commit:
            post.save()

        """return the post with no corrections without saving it in the database"""
        return post


class PostCreateForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyFieldsMixin, PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('image', None)  # remove image from form


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search for posts...'},
        )
    )


class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add a comment...'
                }
            )
        }


"""if extra=2 - two equals forms, extra=3 ..."""
CommentFromSet = formset_factory(CommentFrom, extra=1)
