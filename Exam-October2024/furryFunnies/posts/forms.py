from django import forms

from common.mixins import ReadOnlyMixin
from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at', 'author']

        labels = {
            'title': 'Title',
            'image_url': 'Post Image URL',
            'content': 'Content',
        }

        help_texts = {
            'image_url': 'Share your funniest furry photo URL!',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
        }

class PostCreateForm(PostBaseForm):
    pass

class PostEditForm(PostBaseForm):
    pass

class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    read_only_fields = ['title', 'image_url', 'content']