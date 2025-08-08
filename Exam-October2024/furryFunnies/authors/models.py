from django.core.validators import MinLengthValidator
from django.db import models

from authors.validators import LettersOnlyValidator, SixDigitsExactValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            LettersOnlyValidator(),
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            LettersOnlyValidator(),
        ]
    )
    passcode = models.CharField(
        max_length=6,
        help_text="Your passcode must be a combination of 6 digits",
        validators=[
            SixDigitsExactValidator(),
        ]
    )
    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
