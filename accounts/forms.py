from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
User = settings.AUTH_USER_MODEL

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Full name")

    class Meta:
        model = User
        fields = ("username", "fullname", "email", )

    def save(self, *args, **kwargs):
        import pdb
        pdb.set_trace()
        user = super().save(*args, **kwargs)
        