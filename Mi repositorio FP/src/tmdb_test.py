from tmdb import *

PELICULAS = leer_peliculas('doc/examenes/datos/peliculas.csv', 'doc/examenes/datos/generos.csv')

print(len(PELICULAS))
print(PELICULAS[0])

print(genero_mas_frecuente(PELICULAS))