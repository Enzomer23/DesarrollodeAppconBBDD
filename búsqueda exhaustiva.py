def busqueda_exhaustiva():
    mejor_posicion = None
    mejor_distancia = float('inf')
    
    for posicion in range(-10, 11):
        distancia = calcular_distancia(posicion)
        
        if distancia < mejor_distancia:
            mejor_distancia = distancia
            mejor_posicion = posicion
    
    return mejor_posicion

def calcular_distancia(posicion):
    pass

mejor_posicion = busqueda_exhaustiva()
print("Mejor posición de montaje encontrada:", mejor_posicion)
