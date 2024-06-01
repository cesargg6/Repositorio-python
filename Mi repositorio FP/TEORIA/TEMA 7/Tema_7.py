#lectura y conversion de datos
cadena = "123"

numero = int(cadena)
print(f"El valor entero de la cadena '{cadena}' es: {numero}")

print("\n-----------\n")
print("CONVERTIR STR A DATETIME")
#convertir str a datetime
from datetime import datetime
cadena = "13/11/2020"

fecha = datetime.strptime(cadena, "%d/%m/%Y").date()
print(f"El objeto date para la fecha '{cadena}' es: {fecha}")

print("-----")

cadena = "7-55-27"

hora = datetime.strptime(cadena, "%H-%M-%S").time()
print(f"El objeto time para la hora '{cadena}' es: {hora}")

print("--------")

cadena = "11/13/2020-7:55:27"

fechahora = datetime.strptime(cadena, "%m/%d/%Y-%H:%M:%S")
print(f"El objeto datetime para la fecha y hora '{cadena}' es: {fechahora}")


#valores booleanos
print("\n-----------\n")
print("VALORES BOOLEANOS")
cadena = 'NO'

if cadena == 'SI':
    booleano = True
else:
    booleano = False
print(f"El valor booleano de la cadena '{cadena}' es: {booleano}")

#lectura y compresion de dicheros csv con trasformacion
from collections import namedtuple

Autobus = namedtuple('Autobus', 'matricula, fabricante, inicio, capacidad, \
    asientos, kilometros, articulado')
import csv

def lee_autobuses(nombre_fichero):
    autobuses = []
    with open(nombre_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for matricula, fabricante, inicio, capacidad, asientos, kilometros, articulado in lector:
            inicio = parse_date(inicio)
            capacidad = int(capacidad)
            asientos = int (asientos)
            kilometros = float(kilometros)
            articulado = parse_bool(articulado)
            tupla = Autobus(matricula, fabricante, inicio, capacidad, asientos, \
                            kilometros, articulado)
            autobuses.append(tupla)
    return autobuses

autobuses = lee_autobuses("tussam.csv")
print("Los tres primeros autobuses son:\n", autobuses[:3])
print("\nLos tres últimos autobuses son:\n", autobuses[-3:])