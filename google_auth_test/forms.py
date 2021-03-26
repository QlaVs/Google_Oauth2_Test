from django import forms
from .models import Curr_User


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Curr_User
        fields = ['name', 'image', 'user_info']
