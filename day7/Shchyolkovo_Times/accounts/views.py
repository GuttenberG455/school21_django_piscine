from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.
from accounts.forms import *


def log_in(request, form):
    username = form.cleaned_data.get('username_nav')
    raw_password = form.cleaned_data.get('password_nav')
    user = auth.authenticate(username=username, password=raw_password)
    if user and user.is_active:
        auth.login(request, user)
        return True
    return False


def render_log_in(request):
    if request.user.id is not None:
        auth.logout(request)
    form = AuthorizationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        if log_in(request, form):
            return redirect("go_home")
    return render(request, "accounts/login.html", locals())


def render_sign_up(request):
    form = AuthorizationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        if log_in(request, form):
            return redirect("go_home")
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect("go_home")
    else:
        reg_form = RegistrationForm()
    return render(request, "accounts/registration.html", locals())


def log_out(request):
    auth.logout(request)
    return redirect('go_home')
