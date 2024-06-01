from videojuegos import *
from typing import * 

def test_dicc_porcentaje_ventasJP_por_anyo(listado: list[Juego]):
    print(dicc_porcentaje_ventasJP_por_anyo(listado))

def test_ventas_por_anyo(listado: list[Juego]):
    print(ventas_por_anyo(listado))

def test_genero_mas_presente(listado: list[Juego]):
    print(genero_mas_presente(listado))

def test_mayor_dif_NA_EU(listado: list[Juego]):
    print(mayor_dif_NA_EU(listado))

def test_incremento_ventas(listado: list[Juego]):
    print(incremento_ventas(listado))

def  test_juego_mas_ventas_globales_saga(listado: list[Juego], saga: str):
    print('Juego saga ', saga, ' más ventas globales',  juego_mas_ventas_globales_saga(listado, saga))

def test_primer_juego_distinto(listado: list[Juego])->None:
    print(primer_juego_distinto(listado))

def main():
    GAMES = lee_videojuegos(
        'data/videojuegos.csv')
    #print(GAMES[:2])
    #print('data' in 'data/videojuegos_short.csv')
    #print('foo' in 'data/videojuegos_short.csv')
    #test_ventas_por_anyo(GAMES)
    #test_dicc_porcentaje_ventasJP_por_anyo(GAMES)
    #test_genero_mas_presente(GAMES)
    #test_mayor_dif_NA_EU(GAMES)
    #test_incremento_ventas(GAMES)
    #test_juego_mas_ventas_globales_saga(GAMES, 'Pokemon')
    #test_juego_mas_ventas_globales_saga(GAMES, 'Mario')
    test_primer_juego_distinto(GAMES)

if __name__ == '__main__':
    main()
