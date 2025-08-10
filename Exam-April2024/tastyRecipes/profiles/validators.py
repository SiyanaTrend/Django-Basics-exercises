from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CapitalLetterValidator:
    def __init__(self, message: str = None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value or "Name must start with a capital letter!"

    def __call__(self, value: str, *args, **kwargs):
        if not value[0].isupper():
            raise ValidationError(self.message)
