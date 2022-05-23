import psycopg2
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from d05 import settings


def init(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        curs = conn.cursor()
        curs.execute("""
        CREATE TABLE ex06_movies(
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb INT PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
            created TIMESTAMP NOT NULL DEFAULT NOW(),
            updated TIMESTAMP NOT NULL DEFAULT NOW()
            );
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON {self.TABLE_NAME} FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
        """)
        conn.commit()
        if curs and not curs.closed:
            curs.close()
    except Exception as e:
        return HttpResponse(e)
    finally:
        if conn and not conn.closed:
            conn.close()
    return HttpResponse("OK")


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
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        curs = conn.cursor()
        for movie in data:
            try:
                curs.execute("""
                            INSERT INTO ex04_movies 
                            (title, episode_nb, opening_crawl,
                             director, producer, release_date) 
                            VALUES (%(title)s, %(episode_nb)s, %(opening_crawl)s, 
                            %(director)s, %(producer)s, %(release_date)s)""", movie)
                conn.commit()
            except Exception as e:
                print('Error : ', e)
        if curs and not curs.closed:
            curs.close()
    except Exception as e:
        return HttpResponse(e)
    finally:
        if conn and not conn.closed:
            conn.close()
    return HttpResponse("OK")


def display(request):
    movies_list = None
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        cursor = conn.cursor()
        cursor.execute("""SELECT
                    episode_nb,
                    title,
                    opening_crawl,
                    director,
                    producer,
                    release_date,
                    created,
                    updated
                    from ex06_movies
                    ORDER BY episode_nb""")
        movies_list = cursor.fetchall()
    except Exception as e:
        print('Error : ', e)
        return HttpResponse("No data available")
    finally:
        if conn and not conn.closed:
            conn.close()
    if movies_list:
        return render(request, 'ex06/display_moviesSQL.html', locals())
    else:
        return HttpResponse("No data available")

def update(request):
    