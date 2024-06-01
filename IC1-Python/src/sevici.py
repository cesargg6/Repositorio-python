from collections import namedtuple
from math import sqrt
from typing import NamedTuple, List, Tuple

import folium
from coordenadas import Coordenada, calcula_distancia

#Estacion = namedtuple('Estacion','name,slots,empty_slots,free_bikes,latitude,longitude')
class Estacion(NamedTuple):
    name: str
    slots: int
    empty_slots: int
    free_bikes: int
    coordenada:Coordenada

DELIMITADOR = ','

            
def lee_estaciones(ruta:str)->List[Estacion]:
    result = []
    with open(ruta, encoding='UTF-8') as file:
        for linea in file:
            result.append(linea)
    return transforma_a_estaciones(result[1:])

def transforma_a_estaciones(lista_lineas: List[str])->List[Estacion]:
    result = []
    for linea in lista_lineas:
        splits = linea.split(DELIMITADOR)
        name = splits[0].strip()
        slots = int(splits[1].strip())
        empty_slots = int(splits[2])
        free_bikes= int(splits[3])
        latitude = float(splits[4])
        longitude = float(splits[5])
        coordenada = Coordenada(latitude, longitude)
        result.append(Estacion(name,slots,empty_slots,free_bikes,
                    coordenada))
    return result

def estaciones_bicis_libres(estaciones:List[Estacion], k:int=5)->List[Tuple[int, str]]:
    ''' Devuelve las estaciones que tienen k bicicletas libres
    
    ENTRADA: 
      @param estaciones: lista de estaciones disponibles 
      @type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
      @param k: número mínimo requerido de bicicletas
      @type k: int
    SALIDA: 
      @return: lista de estaciones seleccionadas
      @rtype: [(int, str)] 
    
    Toma como entrada una lista de estaciones y un número k.
    Crea una lista formada por tuplas (número de bicicletas libres, nombre)
    de las estaciones que tienen al menos k bicicletas libres. La lista
    estará ordenada por el número de bicicletas libres.
    '''
    
    listado_salida = selecciona_estaciones_bicis_libres(estaciones, k)
    lista = transforma_estacion_a_freebikes_name(listado_salida)
    return sorted(lista)

def transforma_estacion_a_freebikes_name(
        listado: List[Estacion])->List[Tuple[int, str]]:
    result = []
    for e in listado:
        result.append((e.free_bikes, e.name))
    return result

def selecciona_estaciones_bicis_libres(
        estaciones:List[Estacion], k:int=5)->List[Estacion]:
    result = []

    for e in estaciones:
        if e.free_bikes >= k:
            result.append(e)
    return result



def estaciones_cercanas(estaciones:List[Estacion], 
                        coordenadas: Coordenada, 
                        k:int=5)->List[Tuple[float, str, int]]:
    ''' Estaciones cercanas a un punto dado
    
    ENTRADA: 
      @param estaciones: lista de estaciones disponibles
      @type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
      @param coordenadas: coordenadas formada por la latitud y la longitud de un punto
      @type coordenadas: Coordenadas(float, float)
      @param k: número de estaciones cercanas a calcular 
      @type k: int
    SALIDA: 
      @return: Una lista de tuplas con la distancia, nombre y bicicletas libres de las estaciones seleccionadas 
      @rtype: [(float, str, int)] 
    
    Toma como entrada una lista de estaciones, 
    las coordenadas de  un punto y
    un valor k.
    Crea una lista formada por tuplas (distancia, nombre de estación, 
    bicicletas libres)
    con las k estaciones con bicicletas libres más cercanas al punto dado, 
    ordenadas por
    su distancia a las coordenadas dadas como parámetro.
    '''
    result = []

    for e in estaciones:
        distancia = calcula_distancia(coordenadas, e.coordenada)
        result.append((distancia, e.name, e.free_bikes))

    result = sorted(result)

    return result[:k]

def media_coordenadas (estaciones:List[Estacion])->Coordenada:
    '''Devuelve una coordenada cuya latitud es la media de las latitudes y
    cuya longitud es la media de las longitudes.
    ENTRADA
        @param estaciones: lista de estaciones disponibles
        @ptype estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
    SALIDA
        @return: Una coordenada cuya longitud es la media de las longitudes, y la 
             latitud la media de las latitudes
        @rtype: Coordenadas(float, float)
    '''
    latitudes = [e.coordenada.latitude for e in estaciones]
    longitudes = [e.coordenada.longitude for e in estaciones]
    suma_latitudes = sum(latitudes)
    suma_longitudes = sum(longitudes)

    if len(estaciones)>0:
        result = Coordenada(suma_latitudes/len(latitudes), 
                      suma_longitudes/len(longitudes))
    else:
        result = None
    
    return result

def crea_mapa(latitud, longitud, zoom=9):
    '''
    Función que crea un mapa folium que está centrado en la latitud y longitud
    dados como parámetro y mostrado con el nivel de zoom dado.
    ENTRADA:
        @param latitud: latitud del centro del mapa en pantalla
        @type latitud:float
        @param longitud: longitud del centro del mapa  en pantalla
        @type longitud: float
        @param zoom: nivel del zoom con el que se muestra el mapa
        @type zoom: int
    SALIDA:
        @return: objeto mapa creado
        @rtype: folium.Map
    '''
    mapa = folium.Map(location=[latitud, longitud], 
                      zoom_start=zoom)
    return mapa

def crea_marcador (latitud, longitud, etiqueta, color):
    '''
    Función que crea un marcador rojo con un icono de tipo señal de información.
    El marcador se mostrará en el punto del mapa dado por la latitud y longitud
    y cuandos se mueva el ratón sobre él, se mostrará una etiqueta con el texto
    dado por el parámetro etiqueta
    ENTRADA:
        @param latitud: latitud del marcador
        @type latitud: float
        @param longitud: longitud del marcador
        @type longitud: float
        @param etiqueta: texto de la etiqueta que se asociará al marcador 
        @type etiqueta: str
    SALIDA:
        @return: objeto marcador creado
        @rtype:folium.Marker
    '''
    marcador = folium.Marker([latitud,longitud], 
                   popup=etiqueta, 
                   icon=folium.Icon(color=color, icon='info-sign')) 
    return marcador

def crea_mapa_estaciones(estaciones:List[Estacion], funcion_color):
    '''Genera un objeto de tipo folium.Map con un marcador por cada
    estación dada como parámetro. El marcador tendrá como etiqueta
    el nombre de la estación, y su color se obtendrá a partir de la 
    función ```funcion_color``` que se pasa como parámetro
    ENTRADA
        @param estaciones: lista de estaciones disponibles
        @type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
        @param funcion_color: Función que se aplica a una estación y devuelve una cadena
            que representa el color en el que se dibuja el marcador
        @type funcion_color: function(Estacion)->str
    SALIDA
        @return: objeto mapa creado con los marcadores
        @rtype: folium.Map
    '''
    #Calculamos la media de las coordenadas de las estaciones, para poder centrar el 
    #mapa
    centro_mapa = media_coordenadas(estaciones)
    # creamos el mapa con folium
    mapa = crea_mapa(centro_mapa.latitude, centro_mapa.longitude, 13)

    for estacion in estaciones:
        etiqueta = estacion.name
        color = funcion_color(estacion)
        marcador = crea_marcador (estacion.coordenada.latitude, estacion.coordenada.longitude, etiqueta, color)
        marcador.add_to(mapa)
    
    return mapa

def color_azul(estacion):
   '''Función que devuelve siempre azul
   ENTRADA
      @param estacion: Estación para la que quiero averiguar el color
      @type estacion: Estacion(str, int, int, int, Coordenadas(float, float))
   SALIDA
      @return: El color azul
      @rtype: str
   '''
   return "blue"