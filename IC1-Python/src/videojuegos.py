import datetime
from typing import Dict, NamedTuple
import csv
from collections import Counter, defaultdict

DELIMITADOR = ','

'''class Juego(NamedTuple):
    rank:int 
    name:str
    platform:str
    year:int
    genre:str 
    publisher:str
    NA_sales:float
    EU_sales:float
    JP_sales:float
    other_sales:float
    global_sales:float
'''

Juego = NamedTuple('Juego', [('rank', int), ('name', str), ('platform', str), 
                             ('year', int), ('genre', str), ('publisher', str), 
                             ('NA_sales', float), 
                             ('EU_sales', float), ('JP_sales', float), 
                             ('other_sales', float),
                             ('global_sales', float)])


def lee_videojuegos(ruta:str, codificacion:str='UTF-8')->list[Juego]:
    result = []
    with open(ruta, encoding = codificacion) as f:
        lector = csv.reader(f)
        next(lector)
        for splits in lector:
            rank = int(splits[0].strip())
            name = splits[1].strip()
            platform = splits[2].strip()
            year = int(splits[3])
            genre = splits[4].strip()
            publisher = splits[5].strip()
            na_sales = float(splits[6])
            eu_sales = float(splits[7])
            jp_sales = float(splits[8])
            other_sales = float(splits[9])
            global_sales = float(splits[10])
            result.append(Juego(rank,name,platform,year,genre,
                        publisher,na_sales,eu_sales,jp_sales,
                        other_sales,global_sales))
    return result


def num_juegos_mas_ventasJP(lista_juegos:list[Juego])->int:
    '''num_juegos_mas_ventasJP(lista_juegos): 
    calcula cuántos videojuegos han tenido más ventas en Japón 
    que en Norteamérica.'''
    result = []
    for j in lista_juegos:
        if j.JP_sales>j.NA_sales:
            result.append(j)
    return len(result)

def juegos_distribuidora_anyo(lista_juegos:list[Juego], publisher:str, 
                              anyo:int)->list[str]: 
    '''obtiene una lista con los nombres 
    de los juegos de una distribuidora dada en un año dado.'''
    result = []
    for j in lista_juegos:
        if j.year==anyo and j.publisher==publisher:
            result.append(j.name)
    return result

def num_distribuidoras(lista_juegos:list[Juego])->int:
    '''
    obtiene el número de compañías distribuidoras distintas.
    '''
    result = []

    for j in lista_juegos:
        result.append(j.publisher)

    return len(set(result))

def transforma_a_anyo(videojuegos:list[Juego])->list[int]:
    result = []
    for v in videojuegos:
        result.append(v.year)
    return result

def juego_mas_antiguo(lista_juegos:list[Juego])->Juego: 
    '''obtiene el videojuego más antiguo. 
    Si hay empate en el año de publicación se devuelven todos.'''
    anyo_mas_antiguo = min(transforma_a_anyo(lista_juegos)) 
    result = []

    for r in lista_juegos:
        if r.year==anyo_mas_antiguo:
            result.append(r)
    
    return result

def genero_mas_presente(lista_juegos:list[Juego])->str: 
    '''obtiene el género de juego que más veces se repite.'''
    #ESTE EJERCICIO SE RESUELVE CON UN COUNTER
    '''result = dict()

    for j in lista_juegos:
        genero = j.genre
        if genero in result:
            result[genero] += 1
        else:
            result[genero] = 1

    #return max(result.keys(), key = lambda k: result[k])
    return max(result.items(), key = lambda t: t[1])[0]'''
    generos = [j.genre for j in lista_juegos]
    contador = Counter(generos)
    return contador.most_common(1)[0][0]



def genero_mas_ventas(lista_juegos: list[Juego])->str: 
    '''obtiene el género con el global de ventas mayor.'''
    #ESTE EJERCICIO NO ES CORRECTO
    generos = [j.genre for j in lista_juegos]
    counter = Counter(generos)
    return counter.most_common()

def num_juegos_palabra(lista_juegos:list[Juego], palabra:str)->int: 
    '''devuelve el número de juegos que 
    contienen una determinada palabra en el título.'''
    result = []

    for j in lista_juegos:
        if palabra in j.name:
            result.append(j)
    return len(result)


def mayor_dif_NA_EU(lista_juegos:list[Juego])->str:
    '''
    mayor_dif_NA_EU(lista_juegos): obtiene el 
    nombre del videojuego con una mayor diferencia de ventas 
    entre Europa y Norteamérica (a favor de Europa).
    '''
    return max(lista_juegos, key = lambda x:x.EU_sales-x.NA_sales).name

def ventas_por_anyo(lista_juegos:list[Juego])->list[tuple[int, float]]:
    '''ventas_por_año(lista_juegos): devuelve una lista de tuplas 
    formadas por un año 
    y el global de ventas de ese año para los videojuegos que salieron ese año. 
    Ordenada de mayor a menor volumen de venta.
    '''
    result = dict()

    for juego in lista_juegos:
        clave = juego.year
        if clave in result:
            valor = result[clave]
            valor = valor + juego.global_sales
            result[clave] = valor
        else:
            result[clave] = juego.global_sales

    return sorted(result.items(), key = lambda x: x[1], reverse=True)

def dicc_porcentaje_ventasJP_por_anyo(lista_juegos:list[Juego])->dict[int, float]:
    ''' 
    devuelve [una lista ordenada de tuplas (clave, valor)] 
    [diccionario] 
    cuyas claves son los años de publicación 
    de los videojuegos y cuyos valores son los porcentajes 
    de las ventas de los videojuegos en Japón 
    respecto a las ventas globales en ese año. 
    '''
    result = dict()
    auxiliar = dict()

    for juego in lista_juegos:
        if juego.year in result:
            result[juego.year] += juego.JP_sales
            auxiliar[juego.year] += juego.global_sales
        else:
            result[juego.year] = juego.JP_sales
            auxiliar[juego.year] = juego.global_sales

    result = {year: 100.0 * ventas/auxiliar[year] 
              for year, ventas in result.items()}

    return sorted(result.items())


def incremento_ventas(lista_juegos:list[Juego])->list[float]:
    '''
    incremento_ventas(lista_juegos): devuelve una lista ordenada 
    cronológicamente con los incrementos en porcentaje de las ventas 
    globales de los videojuegos que se publicaron un año con respecto al anterior.
    TODO: Clase 21
    '''
    suma_globales_por_anyo = defaultdict(float)
    for juego in lista_juegos:
        suma_globales_por_anyo[juego.year] += juego.global_sales
    items_ordenados = sorted(suma_globales_por_anyo.items())
    #[(1999, 56), (2000, 75)]->[('1999-2000', 100.*19/56),...]
    cremallera = list(zip(items_ordenados, items_ordenados[1:]))

    result = [(str(dato1[0]) + '-' + str(dato2[0]), 100.0*(dato2[1]-dato1[1])/dato1[1]) 
              for dato1, dato2 in cremallera]

    return result





def juego_mas_ventas_globales_saga(lista_juegos:list[Juego], 
                                   saga:str)->tuple[float, str, int]:
    '''
    juego_mas_ventas_globales_saga(lista_juegos, saga): obtiene una tupla formada 
    por las ventas globales, el nombre del juego y el año, 
    del juego de la saga dada como parámetro que más ha vendido. 

    Se considera que un juego pertenece a una saga si en su nombre aparece 
    la palabra dada como parámetro. 
    Por ejemplo, serán juegos de la saga Pokemon aquellos 
    que tengan Pokemon en su nombre.
    '''
    saga_games = [j for j in lista_juegos if saga.lower() in j.name.lower()]
    return max(saga_games, key= lambda x: x.global_sales)

def dicc_ventas_por_zona(lista_juegos: list[Juego], anyo_inicial: int=None, anyo_final:int=None)-> dict[str, float]:
    ''' 
    crea un diccionario con el acumulado de ventas por zona. 
    Las claves del diccionario serán: América, Europa, Japón y Otros, 
    y los valores el total de ventas para esa zona de los años incluidos en el rango 
    (anyo_inicial, anyo_final). 
    Si anyo_inicial es None, se devuelven las ventas acumuladas hasta anyo_final. 
    Si anyo_final es None, se devuelven las ventas acumuladas desde anyo_inicial. 
    Si ambos son None, se acumulan las ventas de todos los años registrados.
    '''
    inicio = anyo_inicial
    if inicio == None:
        inicio = datetime.date.year
    fin = anyo_final
    if fin == None:
        fin = datetime.date.year
    
    juegos = [j for j in lista_juegos if inicio >= j.year >= fin]
    result = defaultdict(float)
    for j in juegos:
        result['América'] += j.NA_sales
        result['Europa'] += j.EU_sales
        result['Japón'] += j.JP_sales
        result['Otros'] += j.other_sales

    return result

def dicc_top_n_juegos_por_genero(lista_juegos:list[Juego], n:int=1)->Dict[str, list[Juego]]:
    '''crea un diccionario cuyas claves son los géneros 
    y cuyos valores son una lista con los n mejores juegos de 
    cada género en formato tupla (posición, nombre). 
    Se considera que un juego es mejor que otro si su posición
    en el ranking es menor. 
    Si no se proporciona ningún número, 
    entonces la lista solo tendrá el juego mejor.'''
    result = dict()

    for juego in lista_juegos:
        clave = juego.genre
        if clave in result:
            lista = result[clave]
            lista.append((juego.rank, juego.name))
            result[clave] = sorted(lista, key = lambda j: j[0])[:n]
            #result[clave].append(juego)
        else:
            result[clave] = [(juego.rank, juego.name)]

    return result


def distribuidora_mas_juegos_genero(lista_juegos: list[Juego], genero:str)->str: 
    '''obtiene el nombre de la distribuidora con más juegos del género dado como parámetro.'''
    distribuidoras = [j.publisher for j in lista_juegos if j.genre==genero]
    return Counter(distribuidoras).most_common(1)[0][0]

def juegos_distinto_ranking_EU_NA(lista_juegos: list[Juego], n:int)->set[Juego]: 
    '''obtiene el conjunto de los videojuegos que están en el ranking
    de los n más vendidos en Norteamérica pero no entre los n más vendidos en Europa,
    o al revés, que están entre los n más vendidos en Europa y no en Norteamérica.'''
    ranking_usa = set(sorted(lista_juegos, lambda x: x.NA_sales, reverse=True)[:n])
    ranking_eu =  set(sorted(lista_juegos, lambda x: x.EU_sales, reverse=True)[:n])

    return ranking_usa.symmetric_difference(ranking_eu)

def juegos_mismo_ranking_EU_NA_JP(lista_juegos: list[Juego], n:int)->set[Juego]: 
    '''obtiene el conjunto de los videojuegos que están simultáneamente entre los n primeros 
    puestos de ventas en Europa, Norteamérica y Japón.'''
    ranking_usa = set(sorted(lista_juegos, lambda x: x.NA_sales, reverse=True)[:n])
    ranking_eu =  set(sorted(lista_juegos, lambda x: x.EU_sales, reverse=True)[:n])
    ranking_jp =  set(sorted(lista_juegos, lambda x: x.JP_sales, reverse=True)[:n])
    return ranking_usa.intersection(ranking_eu).intersection(ranking_jp)


def primer_juego_distinto(lista_juegos: list[Juego])->tuple[Juego, Juego]:
    '''que devuelve una tupla formada por los dos videojuegos 
    de mayor venta que ocupan una posición
    distinta por ventas entre los rankings de Norteamérica y Europa. 
    Por ejemplo, 
    si el ranking de ventas en Norteamérica lo ocupan los videojuegos (X, Y, Z) 
    y el ranking de ventas en Europa lo ocupan los videojuegos (X, Z, V), 
    el resultado sería (Y, Z).'''
    #TODO: Hacer en clase
    ranking_NA = sorted(lista_juegos, key = lambda x: x.NA_sales, reverse=True)
    ranking_EU = sorted(lista_juegos, key = lambda x: x.EU_sales, reverse=True)

    pares = [(posicion, par) for posicion, par in enumerate(zip(ranking_NA, ranking_EU), 1) 
             if par[0] != par[1]]

    return pares[0]

