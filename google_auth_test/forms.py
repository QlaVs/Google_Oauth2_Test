from django import forms
from .models import CurrUser


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CurrUser
        fields = ['name', 'image', 'user_info']
