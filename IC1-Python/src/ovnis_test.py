from ovnis import *
from datetime import datetime

ovnis = lee_avistamientos('data/ovnis.csv', 'UTF-8')
#print(numero_avistamientos_fecha(ovnis, datetime(2011, 7, 4)))


print(hora_mas_avistamientos(ovnis))
print(hora_mas_avistamientos_v2(ovnis))
print(coordenadas_mas_avistamientos(ovnis))