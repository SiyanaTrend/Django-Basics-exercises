from typing import Optional
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

# version 1
# @deconstructible
# class BadLanguageValidator:
#     def __init__(self, bad_words: Optional[list] = None, message: Optional[str] = None):
#         self.bad_words = bad_words or ['pig', 'hippo']
#         self.message = message or 'The text contains bad language!'
#
#     def __call__(self, value: str):
#         for bad_word in self.bad_words:
#             if bad_word.lower() in value.lower():
#                 raise ValidationError(self.message)


# version 2
# @deconstructible
# class BadLanguageValidator:
#     def __init__(self, bad_words: Optional[list] = None, message: Optional[str] = None):
#         self.bad_words = bad_words
#         self.message = message or 'The text contains bad language!'
#
#     @property
#     def bad_words(self):
#         return self.__bad_words
#
#     @bad_words.setter
#     def bad_words(self, value):
#         if value is None:
#             self.__bad_words = ['pig', 'hippo']
#         else:
#             self.__bad_words = value
#
#     def __call__(self, value):
#         if any(bad_word.lower() in value.lower() for bad_word in self.bad_words): # using a generator expression within any()
#             raise ValidationError(self.message)


# version 3
    # prevent misusage of code like, when bad_words is set to 'pig' (a string): validators = BadLanguageValidator('pig').
    # when run the project ValueError would raise in terminal with the message
# @deconstructible
# class BadLanguageValidator:
#     def __init__(self, bad_words=None, message=None):
#         self.bad_words = bad_words
#         self.message = message or 'The text contains bad language!'
#
#     @property
#     def bad_words(self):
#         return self.__bad_words
#
#     @bad_words.setter
#     def bad_words(self, value):
#         if value is None:
#             self.__bad_words = ['pig', 'hippo']
#         elif not isinstance(value, list):               # ensure bad_words is always a list
#             raise ValueError("bad_words must be a list of strings.")
#         else:
#             self.__bad_words = value
#
#     def __call__(self, value):
#         if any(bad_word.lower() in value.lower() for bad_word in self.bad_words):
#             raise ValidationError(self.message)

# version 4
@deconstructible
class BadLanguageValidator:
    def __init__(self, bad_words: Optional[list] = None, message: Optional[str] = None):
        self.bad_words = bad_words or ['pig', 'hippo']
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "The text contains bad language!"

    def __call__(self, value: str):
        for bad_word in value.split():
            if bad_word.lower() in self.bad_words:
                raise ValidationError(self.message)
