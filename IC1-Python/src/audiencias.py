from collections import namedtuple
from typing import List, NamedTuple
import csv

from parsers import parse_boolean

#Audiencia = namedtuple('Audiencia', 'temporada, share')

DELIMITADOR = ','

class Audiencia(NamedTuple):
    temporada:int
    share:float

def lee_audiencias(ruta_fichero:str)->List[Audiencia]:
    result = []
    with open(ruta_fichero, encoding = 'UTF-8') as f:
        lector = csv.reader(f)
        #next(lector)
        for edicion, share in lector:
            temporada = int(edicion)
            share = float(share)
            result.append(Audiencia(temporada, share))
    return result


def seleccion_primera_edicion(listado_audiencias:List[Audiencia])->List[Audiencia]:
    #Primero defino la variable para el sublistado
    result = []
    #Recorro todos los elementos de la secuencia
    for audiencia in listado_audiencias:
        # Defino la condición de filtrado. Si se pasa, acumulo.
        if audiencia[0] == 1:
            result.append(audiencia)

    #Lo último es siempre devolver la "cosa" filtrada
    return result