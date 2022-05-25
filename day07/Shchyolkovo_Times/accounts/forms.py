from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import *


class AuthorizationForm(Form):
    username = CharField(label='username', max_length=100,
                         widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = CharField(label='password',
                         widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
