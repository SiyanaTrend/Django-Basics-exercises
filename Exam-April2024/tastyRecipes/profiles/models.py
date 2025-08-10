from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import CapitalLetterValidator


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2, 'Nickname must be at least 2 chars long!'),
        ],
        unique=True,
    )
    first_name = models.CharField(
        max_length=30,
        validators=[
            CapitalLetterValidator()
        ],
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            CapitalLetterValidator()
        ],
    )
    chef = models.BooleanField(
        default=False,
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nickname

