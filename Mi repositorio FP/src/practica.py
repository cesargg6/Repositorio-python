def lee_fichero(ruta):
    res=[]
    with open(ruta, encoding="UTF-8") as f:
        for i in f:
            res.append(i)
        return res

#print(lee_fichero("data/GH.csv"))
'''
conjunto ={1,2,2,3,4,5,6,7}
lista= [1,2,2,3,4,5,6,7]

conjunto.add(10)
lista[0]=20
diccionario = {"sevila":1,"efgr":3,  "lololo":10}

diccionario.pop("lololo")
diccionario["nuevallave"]=23

print(diccionario)

print(conjunto)
print(lista)
'''



#from collections import namedtuple
#import csv
#from math import sqrt
#from typing import NamedTuple, List, Tuple
#DELIMITADOR = ','

#videojuegos= namedtuple ("videojuegos","Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales")

def lectura_de_fichero(fichero):
    res=[]
    with open(fichero,encoding="utf-8")as f:
        for i in f:
            res.append(i)
        return res[1:]
    
#Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales

def transformacion(lista):
    res=[]
    for i in lista:
        splits=i.split(DELIMITADOR)
        Rank=int(splits[0])
        Name=str(splits[1])
        Platform=str(splits[2])
        Year=int(splits[3])
        Genre=str(splits[4])
        Publisher=str(splits[5])
        NA_Sales=float(splits[6])
        EU_Sales=float(splits[7])
        JP_Sales=float(splits[8])
        Other_Sales=float(splits[9])
        Global_Sales=float(splits[10])
    return res.append(videojuegos(Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales))

#aux= lectura_de_fichero("data/videojuegos_short.csv")
#print(lectura_de_fichero("data/videojuegos_short.csv"))
#print(transformacion(aux))
#print(aux)



























import csv
from typing import NamedTuple, List, Tuple
from coordenadas import Coordenada


###LEER Y TRANSFORMAR
class tupla(NamedTuple):
    name: str
    slots: int
    empty_slots: int
    free_bikes: int
    latitude: float
    longitude: float




def leerytransformar(fichero):
    res=[]
    with open(fichero, encoding="utf-8")as f:
        lector = csv.reader(f)
        next(lector)
        for name, slots, empty_slots, free_bikes, latitude, longitude in lector:
            name=str(name)
            slots=int(slots)
            empty_slots=int(empty_slots)
            free_bikes=int(free_bikes)
            latitude=float(latitude)
            longitude=float(longitude)
            res.append(tupla(name,slots,empty_slots,free_bikes,latitude,longitude))
        return print(res)

#leerytransformar("data\estaciones.csv")


#-------------------------------------

#LEER SOLO
def leer(fichero):
    res=[]
    with open(fichero, encoding="utf-8") as f:
        for linea in f:
            res.append(linea)
        return print(res[1:])

#leer("data\estaciones.csv")


