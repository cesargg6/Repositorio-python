#La función predefinida **sorted** crea una lista ordenada a partir de una secuencia. 
#Se puede aplicar a cualquier secuencia (listas, tuplas o rangos) pero siempre produce una lista como salida.
temperaturas = [23, 23, 28, 29, 25, 24, 20]
print(sorted(temperaturas))
print(sorted(temperaturas, reverse=True))

# Sobre tuplas
print(sorted((3, 1, 2)))

# Sobre rangos
print(sorted(range(20, 10, -1)))


print ("\n-------\n")
# A través del parámetro key podemos indicar el uso de una función de comparación específica. Por ejemplo, 
# podemos indicarle que utilice la función predefinida <code>len</code>, de manera que primero se pasará 
# cada elemento por dicha función y se ordenará la lista según los valores devueltos por esa función

# Ordena la lista de menor a mayor tamaño de las cadenas de texto
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
print(sorted(dias, key=len))


print ("\n-------\n")
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
dias_temps = zip(dias, temperaturas)
#print (list(dias_temps))
# lambda x:x[1] define la función "dada x, devolver x[1]"
print(sorted(dias_temps, key=lambda x: x[1]))
