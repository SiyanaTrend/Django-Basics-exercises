from django import forms


class MyFrom(forms.Form):
    CHOICES = [
        ('1', 'option 1'),
        ('2', 'option 2'),
        ('3', 'option 3'),
    ]

    my_name = forms.CharField(
        max_length=10,
        required=False,
        # initial='Hello',
        label="Put the info:",
        help_text="Put your name",
        widget=forms.Textarea(
            attrs={'cols': 80,
                   'class': 'search-bar',
                   'placeholder': 'Enter the information here!'}
        )
    )

    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
    )

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