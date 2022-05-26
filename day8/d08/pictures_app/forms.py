from django.forms import forms

from pictures_app.models import Image


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('title', 'file')