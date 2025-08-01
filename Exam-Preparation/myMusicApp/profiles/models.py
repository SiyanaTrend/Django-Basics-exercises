from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import AlphaNumericValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator()
        ]
    )
    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
        ]
    )

    # second option if in the tasks is not said to be an integer field
    # age = models.PositiveIntegerField(
    #     blank=True,
    #     null=True,
    # )