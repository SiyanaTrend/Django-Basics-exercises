from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models

from players.validators import LettersDigitsOnlyValidator


class Player(models.Model):
    nickname = models.CharField(
        max_length=60,
        validators=[
            MinLengthValidator(3),
            LettersDigitsOnlyValidator(),
        ],
        unique=True,
        error_messages={
            'unique': 'That nickname is already in use!'
        },
        help_text='*Allowed nicknames contain letters and digits.',
    )
    email = models.CharField(
        max_length=60,
        validators=[
            EmailValidator()
        ],
        unique=True,
        error_messages={
            'unique': 'That email is already registered!'
        },
    )
    achievements = models.TextField(
        blank=True,
        null=True,
        help_text='*Share your achievements.'
    )
    is_pro = models.BooleanField(
        default=False,
    )
