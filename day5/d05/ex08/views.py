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
        curs.execute("""CREATE TABLE IF NOT EXISTS ex08_planets (
                id serial PRIMARY KEY,
                name varchar(64) UNIQUE NOT NULL,
                climate text,
                diameter int,
                orbital_period int,
                population bigint,
                rotation_period int,
                surface_water float,
                terrain varchar(128)
            )""")
        conn.commit()
        curs.execute("""CREATE TABLE IF NOT EXISTS ex08_people (
                id serial PRIMARY KEY,
                name varchar(64) UNIQUE NOT NULL,
                birth_year varchar(32),
                gender varchar(32),
                eye_color varchar(32),
                hair_color varchar(32),
                height int,
                mass float,
                homeworld varchar(64) REFERENCES ex08_planets(name))
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
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        curs = conn.cursor()
        cols1 = ('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period',
                        'surface_water', 'terrain')
        cols2 = ('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height',
                        'mass', 'homeworld')
        with open('static/planets.csv', 'r') as file:
            curs.copy_from(file, 'ex08_planets', columns=cols1, null='NULL')
        with open('static/people.csv', 'r') as file:
            curs.copy_from(file, 'ex08_people', columns=cols2, null='NULL')
        curs.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        return HttpResponse(e)
    finally:
        if conn is not None:
            conn.close()
    return HttpResponse("OK.")


def display(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        curs = conn.cursor()
        curs.execute("""SELECT people.name, people.homeworld, planets.climate  
    FROM ex08_people AS people
    JOIN ex08_planets AS planets ON (people.homeworld = planets.name)
    WHERE planets.CLIMATE LIKE '%windy%'
    ORDER BY people.name
    """)
        people_list = curs.fetchall()
        curs.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError):
        return HttpResponse('No data available')
    finally:
        if conn is not None:
            conn.close()
    if people_list:
        return render(request, 'ex08/displaySQL.html', locals())
    else:
        return HttpResponse('No data available')