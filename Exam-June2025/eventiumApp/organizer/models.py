from django.core.validators import MinLengthValidator
from django.db import models

from organizer.validators import CompanyNameValidator, PhoneNumberValidator, SecretKeyValidator

class Organizer(models.Model):
    company_name = models.CharField(
        max_length=110,
        unique=True,
        validators=[
            CompanyNameValidator(),
            MinLengthValidator(2)
        ],
        help_text="*Allowed names contain letters, digits, spaces, and hyphens."
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[PhoneNumberValidator()],
        error_messages={
            'unique': "That phone number is already in use!"
        }
    )

    secret_key = models.CharField(
        max_length=4,
        validators=[SecretKeyValidator()],
        help_text="*Pick a combination of 4 unique digits."
    )

    website = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.company_name
