from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    lecturer = forms.BooleanField(
        required=True,
    )
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ('title', 'content')
        # exclude = ['content']
        # widgets = {
        #     'title': forms.NumberInput,
        # }
        # help_texts = {
        #     'title': 'Put a title'
        # }
        # labels = {
        #     'title': 'This is title'
        # }
        # error_messages = {
        #     'title': {
        #         'required': '',
        #     }
        # }
        widgets = {
            'language': forms.RadioSelect(
                attrs={'class': 'radio-select'},
            )
        }

# class PostForm(forms.ModelForm) instead of =>
# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#     author = forms.CharField(
#         max_length=30,
#     )
#     created_at = forms.DateTimeField()
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices,
#     )


# Examples:
# class MyFrom(forms.Form):
#     CHOICES = [
#         ('1', 'option 1'),
#         ('2', 'option 2'),
#         ('3', 'option 3'),
#     ]
#
#     my_name = forms.CharField(
#         max_length=10,
#         required=False,
#         # initial='Hello',
#         label="Put the info:",
#         help_text="Put your name",
#         widget=forms.Textarea(
#             attrs={'cols': 40,
#                    'rows': 5,
#                    'class': 'search-bar',
#                    'placeholder': 'Enter the information here!'}
#         )
#     )

    # password = forms.CharField(
    #     required=False,
    #     widget=forms.PasswordInput(),
    # )

    # my_text = forms.CharField(
    #     widget=forms.Textarea()
    # )
    #
    # multiple_select = forms.MultipleChoiceField(
    #     choices=CHOICES,
    #     widget=forms.CheckboxSelectMultiple,
    # )
    #
    # checkbox_field = forms.BooleanField(
    #     required=False,
    # )
    #
    # radio_field = forms.ChoiceField(
    #     choices=CHOICES,
    #     widget=forms.RadioSelect(),
    # )
    #
    # radio_box = forms.CharField(
    #     widget=forms.RadioSelect(choices=CHOICES),
    # )
    #
    # date = forms.DateField(
    #     widget=forms.SelectDateWidget(),
    # )