from django import forms
from . import models

class LoginForm(forms.Form):
    login = forms.CharField(required=True)
    passw = forms.CharField(required=True)
