from sevici import color_azul, crea_mapa_estaciones, estaciones_bicis_libres, lee_estaciones, Estacion
from typing import List

estaciones_sevici:List[Estacion] = lee_estaciones('data/estaciones.csv')

def test_estaciones_libres():
    # Test de la función estaciones_bicis_libres
    libres1 = estaciones_bicis_libres(estaciones_sevici)
    print("Hay", len(libres1), 
          "estaciones con 5 o más bicis libres:", libres1[:5])
    libres2 = estaciones_bicis_libres(estaciones_sevici, 10)
    print("Hay", len(libres2), 
          "estaciones con 10 o más bicis libres:", libres2[:5])
    libres3 = estaciones_bicis_libres(estaciones_sevici, 1)
    print("Hay", len(libres3), 
          "estaciones con al menos una bici libre:", libres3[:5])

def main():
    test_estaciones_libres()

if __name__ == '__main__':
    #main()
    mapa1 = crea_mapa_estaciones(estaciones_sevici, color_azul)
    mapa1.show_in_browser()