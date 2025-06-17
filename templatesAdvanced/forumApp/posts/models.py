from django.db import models

from posts.choices import LanguageChoices
from posts.validators import BadLanguageValidator


class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )
    content = models.TextField(
        validators=[
            BadLanguageValidator(),
        ]
    )
    author = models.CharField(
        max_length=50,
    )
    created_at = models.DateField(
        auto_now_add=True,
    )
    language = models.CharField(
        max_length=20,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER,
    )
