from picos import *


picos = [Pico("Mulhacén", 3479, "Granada"), Pico("Torreón", 1648, "Cádiz"),
         Pico("Peña Santa", 2596, "León"), Pico("Naranjo", 2519, "Asturias"),
         Pico("Alcazaba", 3371, "Granada"), Pico("Veleta", 3396, "Granada"),
         Pico("Torrecilla", 1919, "Málaga"), Pico("Llambrión", 2647, "León"),
         Pico("Teide", 3718, "Santa Cruz de Tenerife"), Pico("Aljibe", 1091, "Cádiz"),
         Pico("Aneto", 3404, "Granada"), Pico("Peña Ubiña", 2417, "León")]

### 1. Obtener un diccionario que relacione cada provincia con los picos de 
# dicha provincia

#print(picos_por_provincia(picos))

'''Resultado esperado: {'Granada': [Pico(nombre='Mulhacén', altitud=3479, provincia='Granada'), 
Pico(nombre='Alcazaba', altitud=3371, provincia='Granada'), Pico(nombre='Veleta', altitud=3396, provincia='Granada'), 
Pico(nombre='Aneto', altitud=3404, provincia='Granada')], 'Cádiz': [Pico(nombre='Torreón', altitud=1648, provincia='Cádiz'), 
Pico(nombre='Aljibe', altitud=1091, provincia='Cádiz')], 'León': [Pico(nombre='Peña Santa', altitud=2596, provincia='León'), 
Pico(nombre='Llambrión', altitud=2647, provincia='León'), 
Pico(nombre='Peña Ubiña', altitud=2417, provincia='León')], 
'Asturias': [Pico(nombre='Naranjo', altitud=2519, provincia='Asturias')], 
'Málaga': [Pico(nombre='Torrecilla', altitud=1919, provincia='Málaga')], 
'Santa Cruz de Tenerife': [Pico(nombre='Teide', altitud=3718, provincia='Santa Cruz de Tenerife')]}'''

### 2. Obtener un diccionario que relacione cada provincia con las altitudes de los 3 picos de mayor altitud de la provincia, de mayor a menor altitud
'''Resultado esperado: {'Granada': [3479, 3404, 3396], 'Cádiz': [1648, 1091], 'León': [2647, 2596, 2417], 
'Asturias': [2519], 'Málaga': [1919], 'Santa Cruz de Tenerife': [3718]}'''

#print(n_alturas_maximas_por_provincia_2(picos))

### 3. Obtener un diccionario que relacione cada provincia con el número de picos de dicha provincia
'''Resultado esperado: {'Granada': 4, 'Cádiz': 2, 'León': 3, 'Asturias': 1, 'Málaga': 1, 'Santa Cruz de Tenerife': 1}'''

#print(num_picos_por_provincia(picos))

### 4. Obtener el número de picos por provincia, usando el tipo Counter
'''Resultado esperado: Counter({'Granada': 4, 'León': 3, 'Cádiz': 2, 'Asturias': 1, 'Málaga': 1, 'Santa Cruz de Tenerife': 1})'''

#print(num_picos_por_provincia_2(picos))

### 5. Obtener un diccionario que relacione cada provincia con la suma de altitudes de los picos de dicha provincia
'''Resultado esperado: {'Granada': 13650, 'Cádiz': 2739, 'León': 7660, 'Asturias': 2519, 'Málaga': 1919, 'Santa Cruz de Tenerife': 3718}'''

#print(suma_alturas_por_provincias(picos))
#print(suma_alturas_por_provincias_2(picos))

### 6. Obtener un diccionario que relacione cada provincia con la altitud media de los picos de dicha provincia
'''Resultado esperado: {'Granada': 3412.5, 'Cádiz': 1369.5, 'León': 2553.3333333333335, 'Asturias': 2519.0, 'Málaga': 1919.0, 'Santa Cruz de Tenerife': 3718.0}'''

#print(altura_media_por_provincias(picos))

### 7. Obtener un diccionario que relacione cada provincia con el pico de mayor altitud de la provincia
'''Resultado esperado: {'Granada': Pico(nombre='Mulhacén', altitud=3479, provincia='Granada'), 'Cádiz': Pico(nombre='Torreón', altitud=1648, provincia='Cádiz'), 
                     'León': Pico(nombre='Llambrión', altitud=2647, provincia='León'), 'Asturias': Pico(nombre='Naranjo', altitud=2519, provincia='Asturias'), 
                     'Málaga': Pico(nombre='Torrecilla', altitud=1919, provincia='Málaga'), 
                     'Santa Cruz de Tenerife': Pico(nombre='Teide', altitud=3718, provincia='Santa Cruz de Tenerife')}'''


#print(obtener_pico_mas_alto_por_provincia(picos))

### 8. Obtener un diccionario que relacione cada provincia con el
#  porcentaje de picos de la provincia respecto al número total de picos
'''Resultado esperado: {'Granada': 33.33333333333333, 'Cádiz': 16.666666666666664, 'León': 25.0, 'Asturias': 8.333333333333332, 
                     'Málaga': 8.333333333333332, 'Santa Cruz de Tenerife': 8.333333333333332}'''

#print(porcentaje_de_picos_por_provincia(picos))

### 9. Obtener la provincia con mayor número de picos
'''Resultado esperado: ('Granada', 4)'''

### 10. Obtener las dos provincias con mayor número de picos, ordenadas de mayor a menor número de picos
'''Resultado esperado: [('Granada', 4), ('León', 3)]'''

### 11. Obtener un diccionario que relacione número de picos con provincias, 
# a partir de otro que relaciona cada provincia con su número de picos
'''Resultado esperado: {4: ['Granada'], 2: ['Cádiz'], 3: ['León'], 1: ['Asturias', 'Málaga', 'Santa Cruz de Tenerife']}'''
#auxiliar = num_picos_por_provincia(picos)
#print(provincias_por_numero_picos(auxiliar))

auxiliar = inicio_nombre_de_pico_por_provincia(picos, 1)
print(invierte_iniciales_picos_por_provincia(auxiliar))