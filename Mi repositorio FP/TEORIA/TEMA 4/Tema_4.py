def imprime_linea(repeticiones = 40, cadena ="_."):
    linea = cadena * repeticiones
    print(linea)
 
#Se pueden usar Funciones como parametros, es decir, se puede guardar en una variable y llamando a la variable eta llama a la funcion:
print("FUNCION COMO PARAMETRO")
funcion = imprime_linea
print("El tipo de la variable función:", type(funcion))
funcion()
print("-------------------")
print("\n LAMBDA \n")

#Funciones sin nombre "lambda"
#lambda n: 2 * n
#lambda n, m: n + m
nombres = ["Ana", "María", "Julia", "Alberto", "Rafa", "Manuel"]
print("Los nombres ordenados alfabéticamente por su última letra:")
print(sorted(nombres, key=lambda n:n[-1]))