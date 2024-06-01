from collections import defaultdict
import csv
from typing import NamedTuple
from datetime import date, datetime

DELIMITADOR = ';'
DELIMITADOR_PARCIAL = '-'

Parcial = NamedTuple('Parcial', [('juegos_j1', int), ('juegos_j2', int)])

PartidoTenis = NamedTuple('PartidoTenis', 
                          [('fecha', date),('jugador1',str),('jugador2', str) ,
                           ('superficie',str), ('resultado', list[Parcial]), 
                           ('errores_nf1', int),('errores_nf2', int)])


def lee_partidos_tenis(fichero: str)->list[PartidoTenis]:
    result = []

    with open(fichero) as f:
        lector = csv.reader(f, delimiter=DELIMITADOR)
        for lista_valores in lector:
            fecha = datetime.strptime(lista_valores[0].strip(), '%d/%m/%Y').date()
            jugador_1 = lista_valores[1].strip()
            jugador_2 =lista_valores[2].strip()
            superficie = lista_valores[3].strip()
            resultado = parsea_set([lista_valores[4], lista_valores[5], lista_valores[6]])
            errores_nf1 = int(lista_valores[7].strip())
            errores_nf2 = int(lista_valores[8].strip())
            result.append(PartidoTenis(fecha, jugador_1, jugador_2, superficie, 
                          resultado, errores_nf1, errores_nf2))

    return result

def parsea_set(parciales: list[str])->list[Parcial]:
    result = []

    for cadena in parciales:
        splits = cadena.split(DELIMITADOR_PARCIAL)
        puntos_1 = int(splits[0])
        puntos_2 = int(splits[1])
        result.append(Parcial(puntos_1, puntos_2))

    return result

def agrega_partidos_por_meses(partidos: list[PartidoTenis])->dict[int, list[PartidoTenis]]:
    result = defaultdict(list)
    for partido in partidos:
        result[partido.fecha.month].append(partido) 
    return result

def partido_mas_errores_por_mes(partidos: list[PartidoTenis], 
                                superficies:list[str] = None)->dict[int, PartidoTenis]:
    filtrados = partidos
    if superficies != None:
        filtrados = [partido for partido in partidos if partido.superficie in superficies]
    
    partidos_por_meses = agrega_partidos_por_meses(filtrados)

    return {mes:max(listado, key = lambda p: p.errores_nf1 + p.errores_nf2) 
            for mes, listado in partidos_por_meses.items()}