from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class LettersOnlyValidator:
    def __init__(self, message: str = None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value or "Your name must contain letters only!"

    def __call__(self, value: str, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)

@deconstructible
class SixDigitsExactValidator:
    def __init__(self, message: str = None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value or "Your passcode must be exactly 6 digits!"

    def __call__(self, value: str, *args, **kwargs):
        if not (value.isdigit() and len(value) == 6):
            raise ValidationError(self.message)
