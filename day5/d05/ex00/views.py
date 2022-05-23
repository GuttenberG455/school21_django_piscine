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
        CREATE TABLE ex00_movies(
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb INT PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
            );
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
