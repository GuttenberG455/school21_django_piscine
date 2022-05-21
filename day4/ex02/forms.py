
from django import forms


class TextForm(forms.Form):
    text_form = forms.CharField(label='Input text')