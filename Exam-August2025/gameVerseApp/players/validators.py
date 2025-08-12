from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LettersDigitsOnlyValidator:
    def __init__(self, message: str = 'Nickname must contain only letters and digits!'):
        self.message = message

    def __call__(self, value: str, *args, **kwargs):
        if not value.isalnum():
            raise ValidationError(self.message)
