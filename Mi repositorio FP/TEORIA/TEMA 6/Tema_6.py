#Conjuntos
# 1. Inicializar un conjunto vacío
# NO SE PUEDEN USAR LAS LLAVES, puesto que entonces Python entiende que estamos inicializando un diccionario.
conjunto = set()
print("1. Conjunto vacío:", conjunto)

# 2. Inicializar un conjunto explícitamente
conjunto = {1, 2, 3}
print("2. Conjunto explícito:", conjunto)

# 3. Inicializar un conjunto a partir de los elementos de una secuencia
lista = [1, 5, 5, 2, 2, 4, 3, -4, -1]
conjunto = set(lista)
print("3. Conjunto a partir de secuencia:", conjunto)


#Diccionarios
print("\n")
