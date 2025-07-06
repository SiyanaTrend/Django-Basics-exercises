from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re

@deconstructible
class CompanyNameValidator:
    pattern = re.compile(r"^[A-Za-z0-9\s\-]+$")

    def __call__(self, value):
        if not self.pattern.fullmatch(value):
            raise ValidationError("The company name is invalid!")


@deconstructible
class PhoneNumberValidator:
    def __call__(self, value):
        if not value.isdigit():
            raise ValidationError("")

@deconstructible
class SecretKeyValidator:
    def __call__(self, value):
        if not value.isdigit():
            raise ValidationError("Your secret key must have 4 unique digits!")
        if len(value) != 4:
            raise ValidationError("Your secret key must have 4 unique digits!")
        if len(set(value)) != 4:
            raise ValidationError("Your secret key must have 4 unique digits!")
