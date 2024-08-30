from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['Content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'custom-textarea'}),}
        
