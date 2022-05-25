
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.forms import Form, PasswordInput, CharField


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",  "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        return user


# class LoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(
#         attrs={'autofocus': True, 'class': 'form-control'}),
#     )
#     password = forms.CharField(
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
#     )

class LoginForm(Form):
    username = CharField(label='username', max_length=100)
    password = CharField(label='password', widget=PasswordInput)