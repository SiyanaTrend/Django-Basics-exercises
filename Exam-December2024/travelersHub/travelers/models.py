from django.core.validators import MinLengthValidator
from django.db import models

from travelers.validators import LettersDigitsOnlyValidator


class Traveler(models.Model):
    nickname = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(3),
            LettersDigitsOnlyValidator(),
        ],
        unique=True,
        help_text='*Nicknames can contain only letters and digits.',
    )
    email = models.EmailField(
        max_length=30,
        unique=True,
    )
    country = models.CharField(
        max_length=3,
        validators=[
            MinLengthValidator(3),
        ]
    )
    about_me = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nickname
