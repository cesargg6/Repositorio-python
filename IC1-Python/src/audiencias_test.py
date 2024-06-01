from audiencias import lee_audiencias, seleccion_primera_edicion

listado_1 = lee_audiencias('data/GH.csv')
listado_2 = lee_audiencias('data/MasterChef.csv')

listado_1 = seleccion_primera_edicion(listado_1)
listado_2 = seleccion_primera_edicion(listado_2)

print('GH:', listado_1[0].share)
print('MC:', listado_2[0].share)