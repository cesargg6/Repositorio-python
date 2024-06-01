def area_triangulo(radio):
    area = 3.14159 * (radio**2)
    return area

area1 = area_triangulo(2)
print(area1)

print("\n-------------------------\n")
print("LISTAS")

#Listas para almacenar varios datos en una sola variable
temperaturas = [28.5, 27.8, 29.5, 32.1, 30.7, 25.5, 26.0]
print(temperaturas)
heroes = ["Spiderman", "Iron Man", "Lobezno", "Capitán América", "Hulk"]
print(heroes)

#Tuplas (con parentesis) para almacenar varios datos en una sola variable
print("\n-------------------------\n")
print("TUPLAS")
usuario = ("Mark", "Lenders")
print(usuario)

# Podemos acceder a un elemento concreto, indicando el índice de dicho elemento
print("\n-------------------------\n")
print("ACCEDEMOS A UN ELEMENTO")
print(usuario[1])

#podemos conocer en cualquier momento el número total de elementos dentro de una lista o una tupla mediante la función predefinida **len**:
print("\n-------------------------\n")
print("CONOCER Nº DE ELEMENTOS")
print(len(usuario))

#No podemos asignar valores a las posiciones de una tupla, pero si a una lista
print("\n-------------------------\n")
print("ASIGNAR VALOR A UNA LISTA")
heroes[0] = "jose"
print (heroes)

#Podemos crear una lista con tuplas en su interior

print("\n-------------------------\n")
print("LISTA CON TUPLAS EN SU INTERIOR")
listatuplas=[("jose","perez"),("paco","garcia"),("maría","gutierrez")]
print(listatuplas)
print(listatuplas[0])#Seleccion 1º elemento de la lista (en este caso es la tupla)
print(listatuplas[0][1])#seleccion primer elemento de la lista y primer elemento de la tupla

#Diccionarios, cada valor lleva asociado una clave
print("\n-------------------------\n")
print("DICCIONARIOS")
temperatura_media = {"Almería": 19.9, "Cádiz": 19.1, "Córdoba": 19.1, "Granada": 16.6, 
                     "Jaén": 18.2, "Huelva": 19.0, "Málaga": 19.8, "Sevilla": 20.0}
print(temperatura_media)
print("Temperatura anterior:", temperatura_media['Sevilla'])
temperatura_media['Sevilla'] = 1.0   # ¡Cambio climático!
print("Temperatura actual:", temperatura_media['Sevilla'])


contraseñas = {"Ruben": 23, "Claudia": 22, "Dario": 45}
print(contraseñas)
print(contraseñas["Ruben"])
contraseñas[23]="rubena"
print(contraseñas[23])

#Objetos, si queremos añadir un elemento al final de una lista/tupla podemos hacerlo con  .append
print("\n-------------------------\n")
print("OBJETOS")
temperaturas.append(29.2)  # añade el valor 29.2 al final de la lista
print(temperaturas)
print(len(temperaturas))

#Bucles for
print("\n-------------------------\n")
print("BUCLE FOR")

for temperatura in temperaturas:
    print("La temperatura es:", temperatura)


#Ficheros
import csv
print("\n-------------------------\n")
print("FICHEROS")
with open("data/estaciones.csv", encoding='utf-8') as f:
    for linea in f:
        print(linea)