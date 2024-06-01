# Videojuegos

## **Autores**: Antonia M. Reina y José C. Riquelme.      **Revisores**: Mariano González.     **Última modificación:** 9/1/2020

Este ejercicio está basado en el ejercicio propuesto en el primer examen práctico de la asignatura en el curso 2018/19, realizado el 1 de febrero de 2019. Los apartados que aparecían en el examen son los que figuran con una puntuación.
Disponemos de un conjunto de datos con información sobre ventas de videojuegos. Los datos se encuentran almacenados en un fichero en formato CSV codificado en UTF-8. Cada registro del fichero ocupa una línea y contiene los datos correspondientes a un videojuego: posición en el ranking de ventas, nombre del videojuego, plataforma, año de salida al mercado, género, compañía distribuidora, volumen de ventas en Norteamérica, Europa, Japón y otras zonas, y volumen global de ventas (el volumen de ventas viene dado en millones de copias).

Estas son las primeras líneas del fichero (<https://bit.ly/2NQLwm8>):

```Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales
1,Wii Sports,Wii,2006,Sports,Nintendo,41.49,29.02,3.77,8.46,82.74
2,Super Mario Bros.,NES,1985,Platform,Nintendo,29.08,3.58,6.81,0.77,40.24
3,Mario Kart Wii,Wii,2008,Racing,Nintendo,15.85,12.88,3.79,3.31,35.82
4,Wii Sports Resort,Wii,2009,Sports,Nintendo,15.75,11.01,3.28,2.96,33
```

Para almacenar estos datos en memoria, utilizaremos tuplas con nombre con la siguiente definición:

```Juego = namedtuple('Juego', 'rank, name, platform, year, genre, publisher, NA_sales, EU_sales, JP_sales, other_sales, global_sales')```

Escribe el código de las funciones que se indican y ejecuta el test correspondiente para probar su funcionamiento. Las soluciones deben ser genéricas y adaptarse a los datos que se reciben como parámetros, sin presuponer unos valores concretos para estos.

* **lee_juegos**(nom_fichero): lee el fichero de entrada y lo almacena en una lista de tuplas.
* **num_juegos_mas_ventasJP**(lista_juegos): calcula cuántos videojuegos han tenido más ventas en Japón que en Norteamérica.
* **juegos_distribuidora_anyo**(lista_juegos, publisher, anyo): obtiene una lista con los nombres de los juegos de una distribuidora dada en un año dado.
* **num_distribuidoras**(lista_juegos): obtiene el número de compañías distribuidoras distintas.
* **juego_mas_antiguo**(lista_juegos): obtiene el videojuego más antiguo. Si hay empate en el año de publicación se devuelven todos.
* **genero_mas_presente**(lista_juegos): obtiene el género de juego que más veces se repite.
* **genero_mas_ventas**(lista_juegos): obtiene el género con el global de ventas mayor.
* **num_juegos_palabra**(lista_juegos, palabra): devuelve el número de juegos que contienen una determinada palabra en el título.
* **mayor_dif_NA_EU**(lista_juegos): obtiene el nombre del videojuego con una mayor diferencia de ventas entre Europa y Norteamérica (a favor de Europa).
* **ventas_por_año**(lista_juegos): devuelve una lista de tuplas formadas por un año y el global de ventas de ese año para los videojuegos que salieron ese año. Ordenada de mayor a menor volumen de venta.
* **dicc_porcentaje_ventasJP_por_año**(lista_juegos): devuelve un diccionario cuyas claves son los años de publicación de los videojuegos y cuyos valores son los porcentajes de las ventas de los videojuegos en Japón respecto a las ventas globales en ese año.
* **incremento_ventas**(lista_juegos): devuelve una lista ordenada cronológicamente con los incrementos en porcentaje de las ventas globales de los videojuegos que se publicaron un año con respecto al anterior.
* **juego_mas_ventas_globales_saga**(lista_juegos, saga): obtiene una tupla formada por las ventas globales, el nombre del juego y el año, del juego de la saga dada como parámetro que más ha vendido. Se considera que un juego pertenece a una saga si en su nombre aparece la palabra dada como parámetro. Por ejemplo, serán juegos de la saga Pokemon aquellos que tengan Pokemon en su nombre.
* **dicc_ventas_por_zona**(lista_juegos, anyo_inicial=None, anyo_final=None): crea un diccionario con el acumulado de ventas por zona. Las claves del diccionario serán: América, Europa, Japón y Otros, y los valores el total de ventas para esa zona de los años incluidos en el rango (anyo_inicial, anyo_final). Si anyo_inicial es *None*, se devuelven las ventas acumuladas hasta anyo_final. Si anyo_final es *None*, se devuelven las ventas acumuladas desde anyo_inicial. Si ambos son *None*, se acumulan las ventas de todos los años registrados.
* **dicc_top_n_juegos_por_genero**(lista_juegos, n=1): crea un diccionario cuyas claves son los géneros y cuyos valores son una lista con los n mejores juegos de cada género en formato tupla (posición, nombre). Se considera que un juego es mejor que otro si su posición en el ranking es menor. Si no se proporciona ningún número, entonces la lista solo tendrá el juego mejor.
* **distribuidora_mas_juegos_genero**(lista_juegos, genero): obtiene el nombre de la distribuidora con más juegos del género dado como parámetro.
* **juegos_distinto_ranking_EU_NA**(lista_juegos, n): obtiene el conjunto de los videojuegos que están en el ranking de los n más vendidos en Norteamérica pero no entre los n más vendidos en Europa, o al revés, que están entre los n más vendidos en Europa y no en Norteamérica.
* **juegos_mismo_ranking_EU_NA_JP**(lista_juegos, n): obtiene el conjunto de los videojuegos que están simultáneamente entre los n primeros puestos de ventas en Europa, Norteamérica y Japón.
* **primer_juego_distinto**(lista_juegos), que devuelve una tupla formada por los dos videojuegos de mayor venta que ocupan una posición distinta por ventas entre los rankings de Norteamérica y Europa. Por ejemplo, si el ranking de ventas en Norteamérica lo ocupan los videojuegos (X, Y, Z) y el ranking de ventas en Europa lo ocupan los videojuegos (X, Z, V), el resultado sería (Y, Z).
