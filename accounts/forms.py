from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    fullname = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["fullname", "email", "username", ]
        help_texts = {'username': None }
