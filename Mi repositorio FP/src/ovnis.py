import locale
import statistics
from typing import NamedTuple, List, Set
from collections import Counter, defaultdict, namedtuple
from datetime import datetime, date

from coordenadas import Coordenada, calcula_distancia


DELIMITADOR = ','

class Avistamiento(NamedTuple):
    datetime:datetime
    city:str
    state:str
    shape:str
    duration:int
    comments:str
    coordenadas:Coordenada

def lee_avistamientos(ruta_fichero, codificacion):
    result = []
    with open(ruta_fichero, encoding = codificacion) as f:
        for linea in f:
            result.append(linea)
    return transforma_linea_a_avistamiento(result[1:])

def transforma_linea_a_avistamiento(lista_linea):
    result = []
    for linea in lista_linea:
        splits = linea.split(DELIMITADOR)
        # Example with the standard date and time format

        fecha = datetime.strptime(splits[0].strip(), '%m/%d/%Y %H:%M')
        city = splits[1].strip()
        state = splits[2].strip()
        shape = splits[3].strip()
        duration = int(splits[4])
        comments = splits[5].strip()
        latitude = float(splits[6])
        longitude = float(splits[7])
        result.append(Avistamiento(fecha,city,state,shape,duration,
                                   comments,
                                   Coordenada(latitude,longitude)))
    return result


def numero_avistamientos_fecha(avistamientos:List[Avistamiento],
                               fecha:datetime)->int:
    '''
    Función que obtiene el número total de avistamientos 
    que se han producido en una fecha determinada, 
    dada por su día, mes y año. 
    Se contarán, por tanto, los avistamientos que hayan tenido 
    lugar a cualquier hora del día. 
    La función recibe una lista de namedtuple de tipo Avistamiento, 
    y una fecha de tipo datetime.date.'''
    result = []

    for a in avistamientos:
        if a.datetime.date() == fecha.date():
            result.append(a)

    return len(result)

def formas_estados(avistamientos: List[Avistamiento], estados: Set[str])->int:
    '''**formas_estados**: Función que obtiene el número de formas 
    distintas que presentaron los avistamientos observados en 
    uno o varios estados. La función recibe una lista de 
    namedtuple de tipo Avistamiento, 
    y un conjunto de estados de tipo _str_.'''

    #result = {a.shape for a in avistamientos if a.state in estados}
    result = []

    for a in avistamientos: 
        if a.state in estados:
            result.append(a.shape)

    return len(set(result))

def duracion_total(avistamientos: List[Avistamiento], estado:str)->int:
    '''**duracion_total**: Función que devuelve la duración total 
    en segundos de los avistamientos que se han observado en un estado. 
    La función recibe una lista de namedtuple de tipo Avistamiento, 
    y un estado de tipo _str_.'''
    filtrados = [a.duration for a in avistamientos if a.state == estado]
    return sum(filtrados)

def distancia(lat_1, long_1, lat_2, long_2):
    return calcula_distancia(Coordenada(lat_1, long_1), 
                             Coordenada(lat_2, long_2))

def avistamientos_cercanos_ubicacion(avistamientos: List[Avistamiento],
                                     coordenada:Coordenada,
                                     distancia:float)->Set[Avistamiento]:
    #* ****: Función que calcula un conjunto con los avistamientos 
    # cercanos a una ubicacion dada. 
    # Concretamente, vamos a obtener los avistamientos 
    # que se encuentren dentro de un determinado radio de distancia 
    # de la ubicación. 
    # La función recibe una lista de namedtuple de tipo Avistamiento, 
    # una ubicación que será una tupla de tipo _(float, float)_, 
    # y una distancia de tipo float.
    return {a for a in avistamientos 
            if calcula_distancia(a.coordenadas, coordenada)<=distancia}
    

'''
### 3. Operaciones con máximos, mínimos y ordenación
'''

def avistamiento_mayor_duracion(avistamientos, forma):
    '''
    Devuelve el avistamiento de mayor duración de entre todos los
    avistamientos de una forma dada.
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @param forma: forma del avistamiento 
    @type forma: str
    @return:  avistamiento más largo de la forma dada
    @rtype: Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))
    '''
    lista_av_forma = []
    for a in avistamientos:
        if a.forma == forma:
            lista_av_forma.append(a)
    av_mayor_duracion = max(lista_av_forma, key = lambda a:a.duracion)
    return av_mayor_duracion

def avistamiento_cercano_mayor_duracion(avistamientos, coordenadas, radio=0.5):
    '''
    Devuelve la duración y los comentarios del avistamiento que más 
    tiempo ha durado de aquellos situados en el entorno de las
    coordenadas que se pasan como parámetro de entrada.
    El resultado debe ser una tupla de la forma (duración, comentarios)
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @param coordenadas: tupla con latitud y longitud
    @type coordenadas: Coordenadas (float, float)
    @param radio: radio de búsqueda
    @type radio: float
    @return: duración y comentarios del avistamiento más largo en el entorno de las coordenadas comentarios del avistamiento más largo
    @rtype: int, str
    '''
    lista_av_cercanos = []
    for a in avistamientos:
        if distancia_haversine(a.coordenadas, coordenadas) < radio:
            lista_av_cercanos.append((a.duracion, a.comentarios))
    return max(lista_av_cercanos)


def avistamiento_cercano_mayor_duracion2(avistamientos, coordenadas, radio=0.5):
    # Por comprensión
    return max ( (a.duracion, a.comentarios) \
                    for a in avistamientos \
                        if distancia_haversine(a.coordenadas, coordenadas) < radio \
    )
    

### 3.3 Avistamientos producidos entre dos fechas

def avistamientos_fechas(avistamientos, fecha_inicial=None, fecha_final=None):
    '''
    Devuelve una lista con los avistamientos que han tenido lugar
    entre fecha_inicial y fecha_final (ambas inclusive). La lista devuelta
    estará ordenada de los avistamientos más recientes a los más antiguos.
    
    Si fecha_inicial es None se devolverán todos los avistamientos
    hasta fecha_final.
    Si fecha_final es None se devolverán todos los avistamientos desde
    fecha_inicial.
    Si ambas fechas son None se devolverá la lista de 
    avistamientos completa. 
    
    Usar el método date() para obtener la fecha de un objeto datetime.
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @param fecha_inicial: fecha a partir de la cual se devuelven los avistamientos
    @type fecha_inicial:datetime.date
    @param fecha_final: fecha hasta la cual se devuelven los avistamientos
    @type fecha_final: datetime.date
    @return: lista de tuplas con la información de los avistamientos en el rango de fechas
    @rtype: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    '''
    # Solución 1: usando datetime.min/max
    if fecha_inicial is None:
        fecha_inicial = datetime.min.date()
    if fecha_final is None:
        fecha_final = datetime.max.date()

    lista = [a for a in avistamientos 
           if fecha_inicial <= a.fechahora.date() <= fecha_final]
    lista.sort(reverse=True)
    return lista

def avistamientos_fechas2(avistamientos, fecha_inicial=None, fecha_final=None):
    # Solución 2: usando una función auxiliar:
    lista = [a for a in avistamientos \
                if fecha_en_rango(a.fechahora.date(), fecha_inicial,fecha_final)]
    lista.sort(reverse=True)
    return lista

def fecha_en_rango(fecha, fecha_inicial=None, fecha_final=None, ):
    res=False
    if fecha_inicial == None and fecha_final == None:
        res = True
    elif fecha_inicial == None:
        res = fecha < fecha_final
    elif fecha_final == None:
        res = fecha_inicial <fecha
    else:
        res = fecha_inicial < fecha < fecha_final
    return res

### 3.4 Avistamiento de un año con el comentario más largo
def comentario_mas_largo(avistamientos, anyo, palabra):
    ''' 
    Devuelve el avistamiento cuyo comentario es el más largo, de entre
    los avistamientos observados en el año dado por el parámetro "anyo"
    y cuyo comentario incluya la palabra recibida en el parámetro "palabra".
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @param anyo: año para el que se hará la búsqueda 
    @type anyo: int
    @param palabra: palabra que debe incluir el comentario del avistamiento buscado 
    @type palabra: str
    @return: avistamiento con el comentario más largo
    @rtype: Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))
    '''    
    lista_avistamientos_anyo_palabra = []
    for a in avistamientos:
        if a.fechahora.year == anyo and palabra in a.comentarios:
            lista_avistamientos_anyo_palabra.append(a)
    return max(lista_avistamientos_anyo_palabra, key=lambda a:len(a.comentarios))
    
def comentario_mas_largo2(avistamientos, anyo, palabra):
    # Por comprensión
    return max((a for a in avistamientos \
                 if a.fechahora.year == anyo and palabra in a.comentarios), \
             key=lambda a:len(a.comentarios)) 


### 3.5 Media de días entre avistamientos consecutivos
def media_dias_entre_avistamientos(avistamientos, anyo=None):
    ''' 
    Devuelve la media de días transcurridos entre dos avistamientos consecutivos.
    Si año es distinto de None, solo se contemplarán los avistamientos del año
    especificado para hacer el cálculo.
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @param anyo: año para el que se hará la búsqueda 
    @type anyo: int
    @return: media de días transcurridos entre avistamientos. Si no se puede realizar el
    cálculo, devuelve None 
    @rtype:-float
    '''    
    fechas = sorted(
            a.fechahora.date() 
                for a in avistamientos 
                    if  anyo == None or a.fechahora.date().year == anyo
    )

    dias_entre_avistamientos = dias_entre_fechas(fechas)
    
    media = None
    if len(dias_entre_avistamientos) > 0:
        media = sum(dias_entre_avistamientos) / len(dias_entre_avistamientos)
    #Cuando no hay datos statistics.mean eleva una excepción
    # try:
    #    media =statistics.mean(dias_entre_avistamientos)
    # except statistics.StatisticsError:
    #     media = None
    return media

def dias_entre_fechas(fechas):
    dias = []
    for f1, f2 in zip(fechas, fechas[1:]):
        dias_f1_f2 = (f2 - f1).days
        dias.append(dias_f1_f2)
    return dias

def dias_entre_fechas2(fechas):
    return [ (f2 - f1).days for f1, f2 in zip(fechas, fechas[:1])  ]

def dias_entre_fechas3(fechas):
    dias = []
    for indx in range(len(fechas)):
        f1 = fechas[indx]
        f2 = fechas [indx+1]
        dias_f1_f2 = (f2 - f1).days
        dias.append(dias_f1_f2)
    return dias

def dias_entre_fechas4(fechas):
    return [ (fechas[indx+1] - fechas[indx]).days for indx in range(len(fechas))]


def avistamientos_por_fecha(avistamientos):
    ''' 
    Devuelve un diccionario que indexa los avistamientos por fechas
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return diccionario en el que las claves son las fechas de los avistamientos 
         y los valores son conjuntos con los avistamientos observados en esa fecha
    @rtype {datetime.date: {Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))}}
    '''
    # Con dict
    av_por_fecha = dict()
    for a in avistamientos:
        f = a.fechahora.date()
        if f in av_por_fecha:
            av_por_fecha[f].add(a)
        else:
            av_por_fecha[f] = {a}
    return av_por_fecha

def avistamientos_por_fecha2(avistamientos):
    # Con defaultdict
    av_por_fecha = defaultdict(set)
    for a in avistamientos:
        av_por_fecha[a.fechahora.date()].add(a)
    return av_por_fecha


def formas_por_mes(avistamientos):
    ''' 
    Devuelve un diccionario que indexa las distintas formas de avistamientos
    por los nombres de los meses en que se observan.
    Por ejemplo, para el mes "Enero" se asociará un conjunto con todas las
    formas distintas observadas en dicho mes.
    
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return: diccionario en el que las claves son los nombres de los meses 
         y los valores son conjuntos con las formas observadas en cada mes
    @rtype {str: {str}}
    '''
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')

    # Con dict
    formas_mes = dict()
    for av in avistamientos:
        clave = av.fechahora.strftime("%B").capitalize()
        if clave in formas_mes:
            formas_mes[clave].add(av.forma)
        else:
            formas_mes[clave]= {av.forma}
    return formas_mes

def formas_por_mes2(avistamientos):
    # Con defaultdict    
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')

    formas_mes = defaultdict(set)
    for av in avistamientos:
        clave = av.fechahora.strftime("%B").capitalize()
        formas_mes [clave].add(av.forma)
    return formas_mes

def numero_avistamientos_por_año(avistamientos):
    '''
    Devuelve el número de avistamientos observados en cada año.
             
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return: diccionario en el que las claves son los años
         y los valores son el número de avistamientos observados en ese año
    @rtype: {int: int}
    '''
    # Con dict
    num_av_por_anyo = dict()
    for a in avistamientos:
        anyo = a.fechahora.year
        if anyo in num_av_por_anyo:
            num_av_por_anyo[anyo] += 1
        else:
            num_av_por_anyo[anyo] = 1
    return num_av_por_anyo

def numero_avistamientos_por_año2(avistamientos):
    # Con Counter
    return Counter(a.fechahora.year for a in avistamientos)

def numero_avistamientos_por_año3(avistamientos):
    # Con defaultdict
    num_av_por_anyo = defaultdict(lambda:0)
    for a in avistamientos:
        anyo = a.fechahora.year
        num_av_por_anyo[anyo]+=1
    return num_av_por_anyo

### 4.4 Número de avistamientos por mes del año
def num_avistamientos_por_mes(avistamientos):
    '''
    Devuelve el número de avistamientos observados en cada mes del año.
    
    Usar la expresión .date().month para obtener el número del mes de un objeto datetime.
    
    Usar como claves los nombres de los doce meses con la inicial en mayúsculas:

    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return:diccionario en el que las claves son los nombres de los meses y 
         los valores son el número de avistamientos observados en ese mes
    @rtype: {str: int}
    '''
    # Con dict
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')
    res = dict()
    for av in avistamientos:
        clave = av.fechahora.strftime("%B").capitalize()
        if clave in res:
            res[clave]+=1
        else:
            res[clave]= 1
    return res

def num_avistamientos_por_mes2(avistamientos):
    # Con Counter
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')

    return Counter(av.fechahora.strftime("%B").capitalize() for av in avistamientos)

def num_avistamientos_por_mes3(avistamientos):
    # Con defaultdict
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')
    res = defaultdict(lambda:0)
    for av in avistamientos:
        clave = av.fechahora.strftime("%B").capitalize()
        res[clave] +=1
    return res

def hora_mas_avistamientos(avistamientos):
    ''' 
    Devuelve la hora del día (de 0 a 23) con mayor número de avistamientos
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return: hora del día en la que se producen más avistamientos
    @rtype: int
       
    En primer lugar construiremos un diccionario cuyas claves sean las horas del
    día en las que se han observado avistamientos, y cuyos valores sean el número
    de avistamientos observados en esa hora.
    Después obtendremos el máximo de los elementos del diccionario según el valor
    del elemento.
    '''
    dicc = dict()
    for a in avistamientos:
        hora = a.fechahora.hour
        if hora in dicc:
            dicc[hora] += 1
        else:
            dicc[hora] = 1
    return max(dicc.keys(), key=dicc.get)

def hora_mas_avistamientos2(avistamientos):
    # Alternativa usando Counter
    c = Counter(a.fechahora.hour for a in avistamientos)
    return c.most_common(1)[0][0]

def longitud_media_comentarios_por_estado(avistamientos):
    '''
    Devuelve un diccionario en el que las claves son los estados donde se
    producen los avistamientos y los valores son la longitud media de los
    comentarios de los avistamientos en cada estado.
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return: diccionario que almacena la longitud media de los comentarios (valores)
         por estado (claves)
    @rtype: {str: float}
            
    En primer lugar creamos un diccionario que agrupe los avistamientos por estado.
    Esto lo hacemos usando una función auxiliar.
    En segundo lugar, creamos un diccionario a partir del primero, en el que se
    calcule la media. Para definir este diccionario usamos una función
    auxiliar que calcule la media de una lista de Avistamientos
    '''
    d = agrupa_avistamientos_por_estado(avistamientos)    
    return {estado: longitud_media_comentarios(lista_avistamientos) \
                for estado, lista_avistamientos in d.items()}      

def agrupa_avistamientos_por_estado(avistamientos):
    '''Devuelve un diccionario en el que las claves son los estados, 
    y los valores listas de avistamientos de ese estado

    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type avistamientos: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return: Un diccionario con estados y listas de avistamientos de ese estado
    :rtype: {str:[Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]}
    '''
    d = {}
    for a in avistamientos:
        clave = a.estado
        if clave in d:
            d[clave].append(a)
        else:
            d[clave] = [a]
    return d


def longitud_media_comentarios(avistamientos):
    '''Dada una lista de avistamientos, devuelve la longitud media de los
    comentarios de esa lista

    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return: La longitud media de los comentarios de la lista
    @rtype: float
    '''
    return statistics.mean(len(a.comentarios) for a in avistamientos)

def porc_avistamientos_por_forma(avistamientos):  
    '''
    Devuelve un diccionario en el que las claves son las formas de los
    avistamientos, y los valores los porcentajes de avistamientos con cada forma.
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return:  diccionario que almacena los porcentajes de avistamientos (valores)
         por forma (claves)
    @rtype: {str: float}
            
    En primer lugar crearemos un diccionario cuyas claves sean las formas
    y cuyos valores sean el número de avistamientos de esa forma.
    Después crearemos un segundo diccionario con las mismas claves y cuyos valores
    resulten de dividir los valores del diccionario anterior por el número
    total de avistamientos, para obtener los porcentajes.
    '''  
    d_contador = {}
    for a in avistamientos:
        clave = a.forma
        if clave in d_contador:
            d_contador[clave] += 1
        else:
            d_contador[clave] = 1
    total_avistamientos = len(avistamientos)
    return {forma: num_avistamientos*100/total_avistamientos \
                for forma, num_avistamientos in d_contador.items()}

def porc_avistamientos_por_forma2(avistamientos):  
    # Solución alternativa con Counter
    d_contador = Counter(a.forma for a in avistamientos)
    total_avistamientos = len(avistamientos)
    return {forma: num_avistamientos*100/total_avistamientos \
                for forma, num_avistamientos in d_contador.items()}

def avistamientos_mayor_duracion_por_estado(avistamientos, n=3):
    '''
    Devuelve un diccionario que almacena los n avistamientos de mayor duración 
    en cada estado, ordenados de mayor a menor duración.
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type avistamientos: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @param n: número de avistamientos a almacenar por cada estado 
    @type n: int
    @return: diccionario en el que las claves son los estados y los valores son listas 
         con los "n" avistamientos de mayor duración de cada estado,
         ordenados de mayor a menor duración
            -> {str: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]}
            
    En primer lugar crearemos un diccionario de agrupación cuyas claves sean los estados
    y cuyos valores sean listas con los avistamientos observados en ese estado.
    Para ello usamos la función auxiliar que definimos en el apartado 4.7.
    Después crearemos un segundo diccionario cuyas claves sean los estados
    y cuyos valores sean las mismas listas, pero en orden de mayor a menor
    duración y recortadas a "n" elementos.
    '''
    avistamientos_por_estado = agrupa_avistamientos_por_estado(avistamientos)
            
    for estado, l_avistamientos in avistamientos_por_estado.items():
        avistamientos_por_estado[estado] = sorted(l_avistamientos, reverse=True, key=lambda a:a.duracion)[:n]
    return avistamientos_por_estado

def avistamientos_mayor_duracion_por_estado2(avistamientos, n=3):
    # Usando una definición por compresión
    avistamientos_por_estado = agrupa_avistamientos_por_estado(avistamientos)
    return {estado:sorted(l_avistamientos, reverse=True, key=lambda a:a.aduracion)[:n] \
                for estado, l_avistamientos in avistamientos_por_estado.items()}

def año_mas_avistamientos_forma(avistamientos, forma):
    '''
    Devuelve el año en el que se han observado más avistamientos
    de una forma dada.
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type avistamientos: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @param forma: forma del avistamiento 
    @type: str
    @return: año con mayor número de avistamientos de la forma dada
    @rtype: int
            
    
    En primer lugar se crea un diccionario con filtro cuyas claves sean los años
    y cuyos valores sean el número de avistamientos observados en ese año,
    utilizando la función ya definida numero_avistamientos_por_año.
    Luego, se calcula el máximo del diccionario según los valores.
    '''
    d = {}
    for a in avistamientos:
        if a.forma == forma: #filtro
            clave = a.fechahora.year
            if clave in d:
                d[clave] +=1
            else:
                d[clave] = 1
    return max(d.keys(), key=d.get)

def año_mas_avistamientos_forma2(avistamientos, forma):
    # con Counter
    avistamientos_año_forma = Counter(a.fechahora.year for a in avistamientos\
                                            if a.forma== forma)
    return avistamientos_año_forma.most_common(1)[0][0]


def estados_mas_avistamientos(avistamientos, n=5):
    '''
    Devuelve una lista con los estados en los que se han observado
    más avistamientos, junto con el número de avistamientos,
    ordenados de mayor a menor número de avistamientos.
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type avistamientos: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @param n: número de estados a devolver 
    @type n: int  
    @return: lista con los estados donde se han observado más avistamientos,
         junto con el número de avistamientos, en orden decreciente
         del número de avistamientos y con un máximo de "limite" estados.
    @rtype: [(str, int)]
            
    En primer lugar crearemos un diccionario cuyas claves sean los estados
    y cuyos valores sean el número de avistamientos observados en ese estado.
    Después crearemos una lista con las claves del diccionario, ordenadas según
    sus respectivos valores en orden decreciente. Finalmente, recortaremos
    esta lista a "limite" elementos.
    '''
    numero_avistamientos_estado = Counter (a.estado for a in avistamientos)
    estados = sorted(numero_avistamientos_estado.items(), key = lambda t:t[1], reverse = True)
    return estados[:n]   

def estados_mas_avistamientos2(avistamientos, n=5):
    #Con most commons
    numero_avistamientos_estado = Counter (a.estado for a in avistamientos)
    estados = numero_avistamientos_estado.most_common(n)
    return estados

def duracion_total_avistamientos_año(avistamientos, estado):
    '''
    Devuelve un diccionario que almacena la duración total de los avistamientos 
    en cada año, para un estado dado.
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type avistamientos: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @param estado: nombre del estado
    @type estado: str
    @return: diccionario en el que las claves son los años y los valores son números 
         con la suma de las duraciones de los avistamientos observados ese año
         en el estado dado
    @rtype: {int: int}

    Se crea un diccionario con filtro cuyas claves sean los años
    y cuyos valores sean la suma de las duraciones de todos los avistamientos
    observados en ese año.
    '''
    duracion_año = dict()
    for a in avistamientos:
        if a.estado == estado:
            clave = a.fechahora.year
            if clave in duracion_año:
                duracion_año[clave] += a.duracion
            else:
                duracion_año[clave] = a.duracion
    return duracion_año

def duracion_total_avistamientos_año2(avistamientos, estado):
    #Con defaultdict
    duracion_año = defaultdict(lambda:0)
    for a in avistamientos:
        if a.estado == estado:
            clave = a.fechahora.year
            if clave in duracion_año:
                duracion_año[clave] += a.duracion
    return duracion_año


def avistamiento_mas_reciente_por_estado(avistamientos):
    '''
    Devuelve un diccionario que almacena la fecha del último avistamiento
    observado en cada estado.
    
    @param avistamientos: lista de tuplas con la información de los avistamientos 
    @type avistamientos: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    @return:  diccionario en el que las claves son los estados y los valores son 
         las fechas del último avistamientos observado en ese estado.
    @rtype: {str: datetime.datetime}
            
    En primer lugar crearemos un diccionario cuyas claves sean los estados
    y cuyos valores sean listas con los avistamientos observados en ese estado.
    Para ello usamos la función auxiliar  definida en el apartado 4.7
    Después crearemos un segundo diccionario cuyas claves sean los estados y
    cuyos valores sean los valores máximos de las listas, según el campo fechahora.
    '''
    d = agrupa_avistamientos_por_estado(avistamientos)
    for estado, lista_avs in d.items():
        m = max(lista_avs, key = lambda a:a.fechahora)
        d[estado]=m.fechahora
    return d

def coordenadas_mas_avistamientos(avistamientos:list[Avistamiento])->Coordenada:
    '''**coordenadas_mas_avistamientos**: Función que devuelve las 
    coordenadas enteras que se corresponden con la zona 
    donde más avistamientos se han observado. 
    Por ejemplo, si hay avistamientos en las coordenadas 
    (40.1, -85.3), (41.13, -85.1) y (40.2, -85.4), 
    la zona con más avistamientos corresponde 
    a las coordenadas enteras (40, -85) con 2 avistamientos.'''
    return Counter(Coordenada(int(r.coordenadas.latitude), int(r.coordenadas.longitude)) 
                   for r in avistamientos).most_common()[0][0]

def hora_mas_avistamientos(avistamientos:list[Avistamiento])->int:
    '''**hora_mas_avistamientos**: 
    Función que devuelve la hora del día (de 0 a 23) 
    en la que se han observado un mayor número de avistamientos.'''
    
    #Agrupando
    result = defaultdict(list)

    for a in avistamientos:
        clave = a.datetime.hour
        result[clave].append(a)
        #result[clave] += [a]
    
    #Transformando    
    return max(result.keys(), key= lambda x: len(result[x]))

def hora_mas_avistamientos_v2(avistamientos:list[Avistamiento])->int:
    '''**hora_mas_avistamientos**: 
    Función que devuelve la hora del día (de 0 a 23) 
    en la que se han observado un mayor número de avistamientos.'''

    #Transformacion

    horas = [a.datetime.hour for a in avistamientos]

    #Agrupando

    result = Counter(horas)
    lista = result.most_common(1)
    if(len(lista)>0):
        result = lista[0][0]
    else:
        result = None
    return result

