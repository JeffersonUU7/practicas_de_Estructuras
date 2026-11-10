def burbuja_optimizado(lista):
    n = len(lista)
    
    for i in range(n):
        # Asumimos que no habrá cambios en esta pasada
        hubo_intercambio = False 
        
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Hacemos el intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # Como sí hubo al menos un cambio, actualizamos la bandera
                hubo_intercambio = True
                
        # Si terminamos de revisar toda la lista y la bandera sigue en False,
        # significa que ya está todo en orden y podemos salirnos del for principal.
        if not hubo_intercambio:
            print(f"Lista ordenada tempranamente en la pasada {i + 1}")
            break
            
    return lista

# Prueba
lista_casi_ordenada = [1, 2, 3, 5, 4, 6, 7]
print(f"Resultado: {burbuja_optimizado(lista_casi_ordenada)}")