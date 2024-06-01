
from collections import Counter, defaultdict
from datetime import date, datetime
from typing import NamedTuple
import csv

Pelicula = NamedTuple('Pelicula', [('id', str)
                                   , ('title', str),
                                   ('original_language', str),
                                   ('release_date', date),
                                   ('vote_average', float),
                                   ('popularity', int),
                                   ('adult', bool),
                                   ('genres', set[str])])

def lee_generos(fichero:str)->dict[str, set[str]]:
    result = defaultdict(set)

    with open(fichero, encoding='UTF-8') as f:
        lector = csv.reader(f, delimiter=':')
        next(lector)
        for id, generos in lector:
            generos = parsea_generos(generos)
            result[id] = result[id].union(generos)
    return result

def parsea_generos(cadena: str)->set[str]:
    result = set()
    trozos = cadena.split(',')
    for split in trozos:
        result.add(split.strip())
    return result

def leer_peliculas(fichero_principal: str, fichero_generos: str)->list[Pelicula]:
    result = []
    generos_por_id = lee_generos(fichero_generos)
    with open(fichero_principal, encoding='UTF-8') as f:
        lector = csv.reader(f)
        next(lector)
        for id,title,original_language,release_date,vote_average,popularity,adult in lector:
            id = id.strip()
            title = title.strip()
            original_language = original_language.strip()
            release_date = datetime.strptime(release_date.strip(), '%Y-%m-%d').date()
            vote_average = float(vote_average)
            popularity = int(popularity)
            adult = preprocesa_bool(adult)
            genres = generos_por_id[id]
            result.append(Pelicula(id,title,original_language,release_date,
                                   vote_average,popularity,
                                   adult, genres))
    return result

def preprocesa_bool(a: str)->bool:
    result = False
    if a.strip().upper() == 'TRUE':
        result = True
    return result


def genero_mas_frecuente(peliculas: list[Pelicula])->tuple[str, int]:
    #Transformación
    result = []
    for p in peliculas:
        result += list(p.genres)
    #Contador (agregación)
    contador = Counter(result)
    return contador.most_common(1)[0]


def media_calificaciones(peliculas: list[Pelicula], conjunto:set[str])->float:
    votos = [p.vote_average for p in peliculas if conjunto.issubset(p.genres)]
    return sum(votos)/len(votos)

'''Escriba una función llamada top_n_por_genero que tome como entrada 
lista de tuplas de tipo Pelicula y un 
valor entero n, y devuelva un diccionario en el que 
las claves sean los géneros y el valor asociado a cada clave 
sea una lista con las n películas de ese género con mayor calificación promedio (vote_average)'''

def top_n_por_genero(peliculas: list[Pelicula], n:int)->dict[str, list[Pelicula]]:
    result = defaultdict(list)
    for p in peliculas:
        claves = p.genres
        for clave in claves:
            listado_valor = result[clave]
            listado_valor.append(p)
            result[clave] = sorted(listado_valor, 
                                   key=lambda pe: pe.vote_average, reverse=True)[:n]
    return result