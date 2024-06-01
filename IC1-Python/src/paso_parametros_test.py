
def test_paso_parametro_1(elemento):
    elemento = elemento + 1 
    print(elemento)

def test_paso_parametro_2(elemento):
    elemento.remove(2)
    print(elemento)

paso_por_copia = 3
paso_por_referencia = [2, 3, 4, 5]

test_paso_parametro_1(paso_por_copia)
print(paso_por_copia)
#ESTO NUNCA ME DEBE PASAR!!!!!!!!!!!!!!
test_paso_parametro_2(paso_por_referencia)
print(paso_por_referencia)