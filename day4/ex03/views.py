from django.shortcuts import render

# Create your views here.

def render_gradient(request):
    step = 255 / 50
    colors_range = []
    for i in range(50):
        colors_range.append(f'{int(i*step):02X}')
    return render(request, 'gradient.html', locals())