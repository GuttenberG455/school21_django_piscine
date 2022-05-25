from django.contrib import auth
from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm


def render_index(request):
    return render(request, "index.html", locals())


def render_sign_up(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save( )
        return redirect("index")
    else:
        errorz = form.errors
    return render(request, "accounts/registration.html", locals())


def render_log_in(request):
    if request.user.id is not None:
        auth.logout(request)
    form = LoginForm(request.POST or None)
    print(request.method, form.is_valid())
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=raw_password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            errormsg = "ERROR NO USER"
            return render(request, "accounts/login.html", locals())
    return render(request, "accounts/login.html", locals())


def logout(request):
    auth.logout(request)
    return redirect("index")


# class Register(FormView):
#     template_name = "accounts/registration.html"
#     form_class = RegisterForm
#     success_url = reverse_lazy('index')
#
#     def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
#         if self.request.user.is_authenticated:
#             messages.error(self.request, 'You already logined!')
#             return redirect('index')
#         return super().get(request, *args, **kwargs)
#
#     def form_valid(self, form: RegisterForm):
#         user = form.save()
#         login(self.request, user)
#         messages.success(self.request, "Registration successful.")
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         messages.error(
#             self.request, "Unsuccessful registration. Invalid information.")
#         return super().form_invalid(form)
