from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class AlphaNumericValidator:
    def __init__(self, message: str=None) -> None:
        self.message = message

    @property
    def message(self) -> str:
        return self.__message

    # @message.setter
    # def message(self, value):
    #     if value is None:
    #         self.__message = "Ensure this value contains only letters, numbers, and underscore."
    #     else:
    #         self.__message = value

    # second option
    @message.setter
    def message(self, value: str) -> None:
            self.__message = value or "Ensure this value contains only letters, numbers, and underscore."


    def __call__(self, value: str, *args, **kwargs) -> None:
        if "-" in value or value.lower() != slugify(value):
            raise ValidationError(self.message)

    # second option
    # def __call__(self, value: str):
    #     if not value.replace("-", "").isalnum():
    #         raise ValidationError(self.message)