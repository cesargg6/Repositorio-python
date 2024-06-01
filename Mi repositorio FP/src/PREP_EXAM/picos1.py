from collections import *
from typing import *

Pico = NamedTuple("Pico", [('nombre', str), ('altitud', int), ('provincia', str)])

### 1. Obtener un diccionario que relacione cada provincia con los picos de dicha provincia

def picos_por_provincia(lista):
    result=defaultdict(list)
    for pico in lista:
        clave = pico.provincia
        result[clave].append(pico)
    return result
        
### 2. Obtener un diccionario que relacione cada provincia con las altitudes de los 3 picos de mayor altitud de la provincia,
# de mayor a menor altitud

def n_alturas_maximas_por_provincia_2(lista):
    result=defaultdict(list)
    #picos_por_provincia que toma la lista de picos y devuelve un diccionario donde las claves son nombres de provincias
    # y los valores son listas de picos asociados a esa provincia.
    picos_por_pr = picos_por_provincia(lista)
    for provin in picos_por_pr.keys():
        result[provin] = sorted([altura.altitud for altura in picos_por_pr[provin]],  reverse=True)
    return result

### 3. Obtener un diccionario que relacione cada provincia con el número de picos de dicha provincia

def num_picos_por_provincia(picos):
    result= defaultdict(list)
    picos_provincia = picos_por_provincia(picos)
    for numero_picos in picos_provincia.keys():
        result[numero_picos]= len(picos_provincia[numero_picos])
    return result

### 4. Obtener el número de picos por provincia, usando el tipo Counter

def num_picos_por_provincia_2(lista):
    result= Counter([pic.provincia for pic in lista])
    return result
    #utiliza Counter para contar la frecuencia de cada provincia, es decir, cada ves que sale el nombre de la provincia lo cuenta
    #(nombre_de_una_provincia=1_pico)

### 5. Obtener un diccionario que relacione cada provincia con la suma de altitudes de los picos de dicha provincia

def suma_alturas_por_provincias(lista):
    result= defaultdict(int)
    picos_por_pr = picos_por_provincia(lista)
    for provincia, picos in picos_por_pr.items():
        result[provincia]=sum([p.altitud for p in picos])
    return result

def suma_alturas_por_provincias_2(lista):
    result = defaultdict(int)
    for picos in lista:
        result[picos.provincia] += picos.altitud
    return result 

### 6. Obtener un diccionario que relacione cada provincia con la altitud media de los picos de dicha provincia

def altura_media_por_provincias(lista):
    result = defaultdict(list)
    suma_por_provincia= suma_alturas_por_provincias(lista)
    numero_picos_por_provincia= num_picos_por_provincia(lista)
    for provincia in suma_por_provincia.keys():
        result[provincia]= (suma_por_provincia[provincia]/numero_picos_por_provincia[provincia])
    return result

### 7. Obtener un diccionario que relacione cada provincia con el pico de mayor altitud de la provincia

def obtener_pico_mas_alto_por_provincia(lista):
    pico_por_pr=picos_por_provincia(lista)
    return {clave:max(valor, key=lambda p:p.altitud) for clave, valor in pico_por_pr.items()}

### 8. Obtener un diccionario que relacione cada provincia con el
#  porcentaje de picos de la provincia respecto al número total de picos

def porcentaje_de_picos_por_provincia(lista):
    picos_por_pr = picos_por_provincia(lista)
    total = len(lista)
    return {clave:100.0*len(valor)/total for clave, valor in picos_por_pr.items()}

### 9. Obtener la provincia con mayor número de picos

def provincia_con_mas_picos(lista):
    num_picos_por_pr = num_picos_por_provincia(lista)
    provincia_max_picos=max(num_picos_por_pr, key=num_picos_por_pr.get)
    return provincia_max_picos

### 10. Obtener las dos provincias con mayor número de picos, ordenadas de mayor a menor número de picos
###MAL
def provincia_mayor_numero_picos(lista):
    picos_por_pr = picos_por_provincia(lista)
    
    return{sorted(picos_por_pr,reverse=True)}
    
### 11. Obtener un diccionario que relacione número de picos con provincias, 
# a partir de otro que relaciona cada provincia con su número de picos

def provincias_por_numero_picos(lista):
    result= defaultdict(list)
    for provincia, numero_picos in lista.items():
        result[numero_picos].append(provincia)
    return result



def inicio_nombre_de_pico_por_provincia(mountains, n):
    result=defaultdict(list)
    aux= picos_por_provincia(mountains)
    for provincia, picos in aux.items():
        result[provincia] =[pico.nombre[:n]for pico in picos]
    return result

def invierte_iniciales_picos_por_provincia(aux):
    result= defaultdict(list)
    for provincia, lista_iniciales in aux.items():
        for inicial in lista_iniciales:
            result[inicial].append(provincia)
    return result