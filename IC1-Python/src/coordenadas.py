from math import sqrt
from typing import NamedTuple

class Coordenada(NamedTuple):
    latitude: float
    longitude: float

def calcula_distancia(coordenadas1:Coordenada, coordenadas2:Coordenada)->float:
    ''' Distancia entre un punto y una estación
    ENTRADA: 
    @param coordenadas1: coordenadas del primer punto
    @type coordenadas1: Coordenadas(float, float)
    @param coordenadas2: coordenadas del segundo punto
    @type coordenadas2: Coordenadas(float, float)
      
    SALIDA: 
    @return: distancia entre dos coordenadas
    @rtype: float 
    
    Toma como entrada dos coordenadas y calcula la distancia entre ambas aplicando la fórmula
    
        distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
    '''
    x1, y1 = coordenadas1
    x2, y2 = coordenadas2
    return sqrt((x2-x1)**2 + (y2-y1)**2)