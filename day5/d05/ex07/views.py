from django.http import HttpResponse
from django.shortcuts import render

from ex07.forms import UpdateForm
from ex07.models import Movies


def populate(request):
    data = [
        {
            'title': "The Phantom Menace",
            'episode_nb': 1,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "Attack of the Clones",
            'episode_nb': 2,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-16"
        },
        {
            'title': "Revenge of the Sith",
            'episode_nb': 3,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-19"
        },
        {
            'title': "A New Hope",
            'episode_nb': 4,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "The Empire Strikes Back",
            'episode_nb': 5,
            'opening_crawl': "",
            'director': "Irvin Kershner",
            'producer': "Gary Kutz, Rick McCallum",
            'release_date': "1980-05-17"
        },
        {
            'title': "Return of the Jedi",
            'episode_nb': 6,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
            'release_date': "1983-05-25"
        },
        {
            'title': "The Force Awakens",
            'episode_nb': 7,
            'opening_crawl': "",
            'director': "J. J. Abrams",
            'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            'release_date': "2015-12-11"
        },
    ]
    for item in data:
        try:
            movie = Movies(title=item['title'], episode_nb=item['episode_nb'], opening_crawl=item['opening_crawl'],
                           director=item['director'], producer=item['producer'], release_date=item['release_date'])
            movie.save()
        except Exception as e:
            print('Error: ', e)
    return HttpResponse("OK")


def display(request):
    movies_list = None
    try:
        movies_list = Movies.objects.all().order_by('episode_nb')
    except Exception as e:
        print('Error : ', e)
        return HttpResponse("No data available")
    if movies_list:
        return render(request, 'ex07/display_moviesOSM.html', locals())
    else:
        return HttpResponse("No data available")


def update(request):
    form = UpdateForm()
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid() and request.POST['select'][0]:
            movie = Movies.objects.get(pk=request.POST['select'][0])
            movie.opening_crawl = request.POST['opening_crawl']
            movie.save()

    movies_list = Movies.objects.all().order_by('episode_nb')
    if movies_list:
        return render(request, 'ex07/updateOSM.html', locals())
    else:
        return HttpResponse("No data available")
