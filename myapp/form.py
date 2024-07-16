from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegisterFrom(UserCreationForm):
    
    username = forms.CharField(help_text=None)
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput,help_text=None,)
    password2 = forms.CharField(label="Password confirmation",widget=forms.PasswordInput, help_text=None,)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your username"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Enter password",}))

class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title','Content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'custom-textarea'}),}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['Content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'custom-textarea'}),}
        
