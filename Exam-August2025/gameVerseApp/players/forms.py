from django import forms
from players.models import Player


class PlayerBaseForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

        labels = {
            'nickname': 'Nickname:',
            'email': 'Email:',
            'achievements': 'Achievements:',
            'is_pro': 'Are you a Pro Player?'
        }

        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': 'Enter your nickname...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter a valid email...'}),
        }


class PlayerCreateForm(PlayerBaseForm):
    class Meta(PlayerBaseForm.Meta):
        exclude = ['achievements']


class PlayerEditForm(PlayerBaseForm):
    class Meta(PlayerBaseForm.Meta):
        exclude = ['email']
