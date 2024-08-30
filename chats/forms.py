from django import forms
from .models import *
from account.models import CustomUser,ProfileModel

class SearchForm(forms.Form):
    username = forms.CharField(label='')


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['bio','gender']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username']