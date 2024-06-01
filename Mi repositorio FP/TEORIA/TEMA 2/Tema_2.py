#Se pueden hacer multiples asignaciones en una única instruccion
print("ASISGANCION MULTIPLE")
edad, peso = 21, 73.2
print(edad)
print(peso)
print("----------")
#intercambio
edad, peso = peso, edad
print(edad)
print(peso)

#Namedtuple
print("\n-------------------\n")
print("NAMEDTUPLE")
from collections import namedtuple
# El primer parámetro que pasamos a namedtuple es el nombre
# que le damos al tipo de tupla que estamos definiendo.
# El segundo parámetro que pasamos a namedtuple indica
# los nombres de cada uno de los elementos de la tupla
Jugador = namedtuple("Jugador", "nombre, apellidos, edad")
#-----------
jugador = Jugador("Mark", "Lenders", 15)
print(jugador)
#en lugar de usar los corchetes e indicar la posición del elemento, utilizamos un punto seguido del nombre del elemento
print("Nombre:", jugador.nombre)
print("Apellidos:", jugador.apellidos)
print("Edad:", jugador.edad)

#Conjutos, permite almacenar datos de cualquier tipo, sin ningún orden determinado, y sin posibilidad de elementos repetidos (set)
print("\n-------------------\n")
print("CONJUNTOS")
temperaturas_conjunto = {32,36,35,36,32,33,34}
print(temperaturas_conjunto)

#Diccionarios, permite almacenar datos de cualquier tipo, sin ningún orden determinado. Cada valor almacenado se asocia a una clave,
#de manera que para acceder a los valores se utilizan dichas claves
print("\n-------------------\n")
print("DICCIONARIOS")
temperaturas_por_provincias = {"Almería": 19.9, "Cádiz": 19.1, "Córdoba": 19.1, "Granada": 16.6, "Jaén": 18.2, "Huelva": 19.0, "Málaga": 19.8, "Sevilla": 20.0}
print("Temperatura en Sevilla:", temperaturas_por_provincias["Sevilla"])
temperaturas_por_provincias["Sevilla"] = 22.0
print(temperaturas_por_provincias)

#Operaciones con contenedores:
print("\n-------------------\n")
print("OPERACIONES CON CONTENEDORES")

#añadir a una lista con .append
temperaturas = [32, 36, 35, 36, 32, 33]
temperaturas.append(65)
print(temperaturas)

#Añadir a un conjunto
temperaturas_conjunto.add(69)
print(temperaturas_conjunto)

#añadir a un diccionario
temperaturas_por_provincias["Badajoz"] = 15.8   # Basta con usar una clave que antes no existía
print(temperaturas_por_provincias)

# Consultar si un elemento forma parte de una tupla, lista, conjunto o diccionario
print(35 in temperaturas)

#para eliminar un elememtno de una lista o deccionario utilizamos (del())
#para un conjunto .remove

print("\n-------------------\n")
print("RECORRER ELEMENTOS POR FOR")

print("tupla jugador")
for j in jugador:
    print(j)

print("\nLista de temperaturas:")
for t in temperaturas:
    print(t)

print("\nConjunto de temperaturas")
for t in temperaturas_conjunto:
    print(t)

print("\nDiccionario de temperaturas por provincias")
for p in temperaturas_por_provincias:
    print(p ,'->',temperaturas_por_provincias[p])

print("\n-------------------\n")
print("TIPOS FECHA Y HORA")

from datetime import date

# Le pasamos al constructor de date el año, el mes y el día, en ese orden
fecha = date(2015, 1, 1)
print(fecha)
# O bien, podemos obtener el día actual, de esta forma
fecha_actual = date.today()
print(fecha_actual)
# Si queremos acceder a cada uno de los campos, usamos los atributos
# day, month y year
print("El día actual es", fecha_actual.day)
print("El mes actual es", fecha_actual.month)
print("El año actual es", fecha_actual.year)

#--------
print("----------")

from datetime import time

# Le pasamos al constructor de date la hora, los minutos y los segundos
hora = time(17, 10, 59)
print(hora)

# Podemos obviar los segundos
hora = time(17,10)
print(hora)
# Si queremos acceder a cada uno de los campos, usamos los atributos
# hour, minute y second
print("El hora es", hora.hour)
print("Los minutos son", hora.minute)
print("Los segundos son", hora.second)

print("\n-------------------\n")
print("FORMATEO DE CADENAS")

a = int(input('Introduce un número:'))
b = int(input('Introduce un número:'))

print('El resultado de {} elevado a {} es {}.'.format(a, b, a**b))







#lectura ficchero, filtrado y transformacion (es lo que va a acare en el examen)


'''frasee="quiero hacer una prueba"
def frase_mayuscula(frase):
    res = []
    for x in frase:
        res.append(x.upper())
    return res

print("".join(frase_mayuscula(frasee)))'''

