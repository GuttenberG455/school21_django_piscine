from django.shortcuts import render, redirect

from day4 import settings
from . import forms
from .log import Logs

# Create your views here.

log = Logs()

def render_form(request):
    text_list = log.get_logs()
    form = forms.TextForm()
    if request.method == 'POST':
        form = forms.TextForm(request.POST)
        if form.is_valid():
            log.write_log(request.POST.get('text_form'))
        return redirect('/ex02')
    return render(request, "form.html", locals())

