from django import forms


class MyFrom(forms.Form):
    my_text = forms.CharField(
        max_length=10,
    )