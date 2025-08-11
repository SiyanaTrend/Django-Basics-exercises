from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class CompanyNameValidator:
    def __init__(self, message: str = "The company name is invalid!"):
        self.message = message

    def __call__(self, value: str, *args, **kwargs):
        for char in value:
            if not (char.isalpha() or char.isdigit() or char in [' ', '-']):
                raise ValidationError(self.message)

    # pattern = re.compile(r"^[A-Za-z0-9\s\-]+$")
    #
    # def __call__(self, value):
    #     if not self.pattern.fullmatch(value):
    #         raise ValidationError("The company name is invalid!")


@deconstructible
class PhoneNumberValidator:

    def __call__(self, value: str, *args, **kwargs):
        if not value.isdigit():
            raise ValidationError("")

    # def __call__(self, value):
    #     if not value.isdigit():
    #         raise ValidationError("")


@deconstructible
class SecretKeyValidator:
    def __init__(self, message: str = "Your secret key must have 4 unique digits!"):
        self.message = message

    def __call__(self, value: str, *args, **kwargs):
        if not (value.isdigit() and len(value) == 4 and len(set(value)) == 4):
            raise ValidationError(self.message)

    # def __call__(self, value):
    #     if not value.isdigit():
    #         raise ValidationError("Your secret key must have 4 unique digits!")
    #     if len(value) != 4:
    #         raise ValidationError("Your secret key must have 4 unique digits!")
    #     if len(set(value)) != 4:
    #         raise ValidationError("Your secret key must have 4 unique digits!")
