from django.shortcuts import render

# Create your views here.

def render_django(req):
    return render(req, "django.html", locals())

def render_display(req):
    return render(req, "display.html", locals())

def render_templates(req):
    river_list = ["Volga", "Dnipro", "Danube", "Ural", "Rhine", "Nile"]
    variable = 42
    var1 = "I am the first variable"
    var2 = "And I am the second"
    return render(req, "templates.html", locals())