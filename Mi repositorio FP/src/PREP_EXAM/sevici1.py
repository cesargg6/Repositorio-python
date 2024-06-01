from collections import *
from typing import *



def lee_estaciones(ruta):
    result=[]
    with open(ruta, encoding="UTF-8") as file:
        next(file)
        for linea in file:
            result.append(linea)
    return result  