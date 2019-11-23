from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AddTweetForm(forms.Form):
    content = forms.CharField(label="Treść tweeta (max 140 znaków)", max_length=140, widget=forms.Textarea)

