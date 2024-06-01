from collections import defaultdict, namedtuple, Counter
from typing import NamedTuple

Pico = NamedTuple("Pico", [('nombre', str), ('altitud', int), ('provincia', str)])

def picos_por_provincia(p: list[Pico])->dict[str, list[Pico]]:
    result = defaultdict(list)
    for pico in p:
        clave = pico.provincia
        result[clave].append(pico)
    return result


def n_alturas_maximas_por_provincia(pics:list[Pico], n:int=3)->dict[str, list[int]]:
    result = defaultdict(list)
    picos_por_pr = picos_por_provincia(pics)
    for provincia in picos_por_pr.keys():
        result[provincia] = sorted([pico.altitud for pico in picos_por_pr[provincia]], reverse=True)[:n]
    return result

def n_alturas_maximas_por_provincia_2(pics:list[Pico], n:int=3)->dict[str, list[int]]:
    result = defaultdict(list)
    for pico in pics:
        provincia = pico.provincia
        result[provincia].append(pico.altitud) 
        result[provincia] = sorted(result[provincia], reverse=True)[:n]
    return result

def num_picos_por_provincia(pics:list[Pico])->dict[str, int]:
    result = defaultdict(int)
    picos_por_pr = picos_por_provincia(pics)
    for provincia in picos_por_pr.keys():
        result[provincia] = len(picos_por_pr[provincia])
    return result

def num_picos_por_provincia_2(pics:list[Pico])->dict[str, int]:
    result = Counter([pico.provincia for pico in pics])
    return result

def suma_alturas_por_provincias(pics:list[Pico])->dict[str, int]:
    result = defaultdict(int)
    picos_por_pr = picos_por_provincia(pics)
    for provincia, picos in picos_por_pr.items():
        result[provincia] = sum(p.altitud for p in picos)
    return result

def suma_alturas_por_provincias_2(pics:list[Pico])->dict[str, int]:
    result = defaultdict(int)
    for pico in pics:
        result[pico.provincia] += pico.altitud
    return result

def altura_media_por_provincias(pics:list[Pico])->dict[str, float]:
    result = defaultdict(float)
    suma_por_provincia = suma_alturas_por_provincias(pics)
    numero_por_provincia = num_picos_por_provincia(pics)
    for provincia in suma_por_provincia.keys():
        result[provincia] = suma_por_provincia[provincia]/numero_por_provincia[provincia]
    return result
    #return {provincia: suma_por_provincia[provincia]/numero_por_provincia[provincia]
    #        for provincia in suma_por_provincia.keys()}

def obtener_pico_mas_alto_por_provincia(mountains: list[Pico])->dict[str, Pico]:
    auxiliar = picos_por_provincia(mountains)
    return {clave:max(valor, key=lambda p: p.altitud) for clave, valor in auxiliar.items()}

def porcentaje_de_picos_por_provincia(mountains: list[Pico])->dict[str, float]:
    auxiliar = picos_por_provincia(mountains)
    total = len(mountains)
    return {clave:100.0*len(valor)/total for clave, valor in auxiliar.items()}

def provincias_por_numero_picos(aux: dict[str, int])->dict[int, list[str]]:
    result = defaultdict(list)

    for provincia, numero_picos in aux.items():
        result[numero_picos].append(provincia)

    return result

def invierte_iniciales_picos_por_provincia(aux: dict[str, list[str]])->dict[str, list[str]]:
    result = defaultdict(list)

    for provincia, lista_iniciales in aux.items():
        for inicial in lista_iniciales:
            result[inicial].append(provincia)

    return result

def inicio_nombre_de_pico_por_provincia(mountains: list[Pico], n: int)->dict[str, list[str]]:
    result = defaultdict(list)
    auxiliar = picos_por_provincia(mountains)
    for provincia, picos in auxiliar.items():
        result[provincia] = [pico.nombre[:n] for pico in picos]

    return result

