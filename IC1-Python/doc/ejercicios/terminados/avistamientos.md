# Avistamientos de OVNIS

## Autores: Daniel Mateos, Mariano González Revisores: Fermín Cruz, Toñi Reina, José C. Riquelme. Última modificación: 7/11/2022

En este ejercicio vamos a trabajar con un conjunto de datos con información sobre avistamientos de objetos voladores no identificados (OVNIs) en los Estados Unidos. El objetivo del ejercicio es leer estos datos y realizar distintas operaciones con ellos. Cada operación se implementará en una función distinta.

Los datos se encuentran almacenados en un fichero en formato CSV codificado en UTF-8. Cada registro del fichero ocupa una línea y contiene los datos correspondientes a un avistamiento: fecha y hora en la que se produjo del avistamiento, ciudad y acrónimo del estado donde se produjo, forma observada del avistamiento, duración en segundos, una descripción textual del avistamiento y la latitud y longitud del lugar donde se produjo.

Estas son las primeras líneas del fichero (acortando la descripción del avistamiento). La primera línea es una cabecera que contiene los nombres de los campos del registro:

```datetime,city,state,shape,duration,comments,latitude,longitude
07/04/2011 22:00,muncie,in,light,240, ((HOAX??)) 4th  of July ufo...,40.1933333,-85.3863889
04/07/2005 17:01,deming (somewhere near),nm,changing,1200, ((NUFORC...,32.2686111,-107.7580556
03/12/2010 19:56,erie,pa,changing,300, 3/12/10Viewed a comet like...,42.1291667,-80.0852778
07/04/2013 22:25,seattle,wa,unknown,600, A RED Light was seen over...,47.6063889,-122.3308333
```

Para almacenar estos datos en memoria, utilizaremos tuplas con nombre con la siguiente definición:

```Avistamiento = namedtuple('Avistamiento', 'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')
```

El objetivo del ejercicio es leer estos datos y realizar distintas operaciones con ellos. Cada operación se implementará en una función distinta. Use funciones auxiliares cuando lo crea conveniente para mejorar la legibilidad del código. Las funciones a implementar son:

### 1. Función de lectura de datos

* **lee_avistamientos**: será la encargada de leer el fichero con los avistamientos y construir a partir de él una estructura de datos en memoria, que será una lista de namedtuple. Esta función recibe la ruta del fichero de tipo _str_. Recordar que cada namedtuple será del tipo 'Avistamiento' definido previamente.

### 2. Operaciones de filtrado, conteo y suma

* **numero_avistamientos_fecha**: Función que obtiene el número total de avistamientos que se han producido en una fecha determinada, dada por su día, mes y año. Se contarán, por tanto, los avistamientos que hayan tenido lugar a cualquier hora del día. La función recibe una lista de namedtuple de tipo Avistamiento, y una fecha de tipo datetime.date.
* **formas_estados**: Función que obtiene el número de formas distintas que presentaron los avistamientos observados en uno o varios estados. La función recibe una lista de namedtuple de tipo Avistamiento, y un conjunto de estados de tipo _str_.
* **duracion_total**: Función que devuelve la duración total en segundos de los avistamientos que se han observado en un estado. La función recibe una lista de namedtuple de tipo Avistamiento, y un estado de tipo _str_.
* **distancia**: Función que calcula la distancia euclidea entre dos coordenadas. La función recibe dos tuplas de tipo _(float, float)_.
* **avistamientos_cercanos_ubicacion**: Función que calcula un conjunto con los avistamientos cercanos a una ubicacion dada. Concretamente, vamos a obtener los avistamientos que se encuentren dentro de un determinado radio de distancia de la ubicación. La función recibe una lista de namedtuple de tipo Avistamiento, una ubicación que será una tupla de tipo _(float, float)_, y una distancia de tipo float.

### 3. Operaciones con máximos, mínimos y ordenación

* **avistamiento_mayor_duracion**: Función que obtiene el avistamiento de mayor duración de entre todos los avistamientos que tienen una forma determinada.La función recibe una lista de namedtuple de tipo Avistamiento y la forma del avistamiento de tipo _str_.
* **avistamiento_cercano_mayor_duracion**: Función que devuelve el avistamiento que más tiempo ha durado de aquellos situados dentro de un radio de distancia de una ubicación dada; es decir, la distancia entre las coordenadas del avistamiento y las coordenadas que se pasan como parámetro de entrada debe ser menor al radio que también aparece como parámetro de la función. El resultado debe ser una tupla de la forma (duración, comentarios). La función recibe una lista de namedtuple de tipo Avistamiento, una coordenada que será una tupla de tipo _(float, float)_, y una distancia de tipo float.
* **avistamientos_fechas**: Función que devuelve una lista con los avistamientos observados entre una fecha inicial y una fecha final, ambas inclusive. La lista devuelta estará ordenada de los avistamientos más recientes a los más antiguos. Si la fecha inicial es _None_, se devolverán todos los avistamientos desde el más antiguo hasta la fecha final. Si la fecha final es _None_, se devolverán todos los avistamientos desde la fecha inicial hasta el más reciente. Si ambas fechas son _None_, se devolverá la lista de avistamientos completa. La función recibe una lista de namedtuple de tipo Avistamiento, y dos fechas de tipo datetime.date: una como principio del intervalo y otra como final. Las fechas recibidas como parámetro tendrán como valor por defecto _None_.
* **comentario_mas_largo**: Función que devuelve el avistamiento con el comentario más largo, de entre todos los avistamientos observados en un año dado y cuyo comentario incluye una palabra concreta. La función recibe una lista de namedtuple de tipo Avistamiento, un año de tipo int, y una palabra de tipo _str_.
* **media_dias_entre_avistamientos**: Función que devuelve la media de días transcurridos entre dos avistamientos consecutivos en el tiempo. La función permite hacer el cálculo para todos los avistamientos, o solo para los de un año concreto. La función recibe una lista de namedtuple de tipo Avistamiento y un año de tipo int.

### 4. Operaciones con diccionarios

* **avistamientos_por_fecha**: Función que crea un diccionario que relaciona las fechas con los avistamientos observados en dichas fechas. Es decir, un diccionario cuyas claves son las fechas y cuyos valores son los conjuntos de avistamientos observados en cada fecha. La función recibe una lista de namedtuple de tipo Avistamiento.
* **formas_por_mes**: Función que devuelve un diccionario que indexa las distintas formas de avistamientos por los nombres de los meses en que se observaron. Por ejemplo, para el mes "Enero" se tendrá un conjunto con todas las formas distintas observadas en dicho mes. La función recibe una lista de namedtuple de tipo Avistamiento.
* **numero_avistamientos_por_año**: Función que crea un diccionario que relaciona cada año con el número de avistamientos observados en dicho año. Es decir, un diccionario cuyas claves son los años y cuyos valores son el número de avistamientos observados en cada año. La función recibe una lista de namedtuple de tipo Avistamiento.
* **num_avistamientos_por_mes**: Función que devuelve el número de avistamientos observados en cada mes del año. Usar como claves los nombres de los doce meses con la inicial en mayúsculas:

```meses = ["Enero", "Febrero", "Marzo",
            "Abril", "Mayo", "Junio", 
            "Julio", "Agosto", "Septiembre", 
            "Octubre", "Noviembre", "Diciembre"]
```

* **coordenadas_mas_avistamientos**: Función que devuelve las coordenadas enteras que se corresponden con la zona donde más avistamientos se han observado. Por ejemplo, si hay avistamientos en las coordenadas (40.1, -85.3), (41.13, -85.1) y (40.2, -85.4), la zona con más avistamientos corresponde a las coordenadas enteras (40, -85) con 2 avistamientos.
* **hora_mas_avistamientos**: Función que devuelve la hora del día (de 0 a 23) en la que se han observado un mayor número de avistamientos.
* **longitud_media_comentarios_por_estado**: Función que devuelve un diccionario en el que las claves son los estados donde se producen los avistamientos, y los valores son la longitud media de los comentarios de los avistamientos observados en cada estado.
* **porc_avistamientos_por_forma**: Función que devuelve un diccionario en el que las claves son las formas de los avistamientos, y los valores son el porcentaje de avistamientos de cada forma con respecto al número total de avistamientos.
* **avistamientos_mayor_duracion_por_estado**: Función que devuelve un diccionario que relaciona los estados con los avistamientos de mayor duración observados en dicho estado, ordenados de mayor a menor duración. Si no se indica nada, se obtendrán los tres avistamientos de mayor duración. La función recibe una lista de namedtuple de tipo Avistamiento y un valor entero que representará el límite que por defecto tendrá el valor 3.
* **año_mas_avistamientos_forma**: Función que devuelve el año en el que se han observado más avistamientos de una forma dada. La función recibe una lista de namedtuple de tipo Avistamiento y la forma a tener en cuenta que será de tipo _str_.
* **estados_mas_avistamientos**: Función que devuelve una lista con el nombre y el número de avistamientos de los estados con mayor número de avistamientos, ordenados de mayor a menor número de avistamientos. Si no se indica nada, se obtendrán los cinco estados con más avistamientos. La función recibe una lista de namedtuple de tipo Avistamiento y un valor entero que representará el límite que por defecto tendrá el valor 3.
* **duracion_total_avistamientos_año**: Función que devuelve un diccionario que relaciona cada año con la suma de las duraciones de todos los avistamientos observados durante ese año en un estado dado. La función recibe una lista de namedtuple de tipo Avistamiento y el estado a tener en cuenta que será de tipo _str_.
* **avistamiento_mas_reciente_estado**: Función que devuelve un diccionario que relaciona cada estado con la fecha del último avistamiento observado en el estado.
