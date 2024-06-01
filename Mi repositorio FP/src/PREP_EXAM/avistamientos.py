from typing import *
from collections import *
from datetime import datetime, date
import csv
from coordenadas import Coordenada
#from coordenadas import Coordenada
#("coordenadas",Coordenada)
#("latitude",float),("longitude",float)

avistamientos= NamedTuple("avistamientos",
                          [("datetime", datetime),
                           ("city",str),("state",str),
                           ("shape",str),("duration",int),
                           ("comments",str),("coordenadas",Coordenada)])

DELIMITADOR=","

def lee_avistamientos(ovnis):
    result=[]
    with open(ovnis, encoding="UTF-8") as f:
        lector=csv.reader(f)
        next(lector)
        for linea in lector:
            result.append(linea)
    return transforma_linea_a_avistamiento(result)

def transforma_linea_a_avistamiento(lista_linea):
    result=[]
    for linea in lista_linea:
        splits=linea.split(DELIMITADOR)
        fecha=datetime.strptime(splits[0].strip(),'%m/%d/%Y %H:%M')
        city=splits[1].strip()
        state=splits[2].strip()
        shape=splits[3].strip()
        duration=splits[4].strip()
        comments=splits[5].strip()
        latitude=splits[5].strip()
        longitude=splits[6].strip()
        result.append(avistamientos(fecha,city,state,shape,duration,comments,Coordenada(latitude,longitude)))
    return result