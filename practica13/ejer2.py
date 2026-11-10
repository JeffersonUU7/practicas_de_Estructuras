def busqueda_binaria_recursiva(lista, objetivo, inicio, fin):
    # Caso base: el rango de búsqueda es inválido, el elemento no está
    if inicio > fin:
        return -1
    
    # Calculamos el punto medio del sub-arreglo actual
    medio = (inicio + fin) // 2
    
    # Caso base de éxito: encontramos el objetivo
    if lista[medio] == objetivo:
        return medio
        
    # Casos recursivos: ajustamos los punteros y volvemos a llamar a la función
    elif lista[medio] < objetivo:
        # Descartamos la mitad izquierda
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)
    else:
        # Descartamos la mitad derecha
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)

# Prueba
lista_ordenada = [10, 25, 32, 45, 58, 61, 79, 82, 95]
objetivo = 61

# Necesitamos pasar el inicio (0) y el fin (len - 1) en la primera llamada
indice = busqueda_binaria_recursiva(lista_ordenada, objetivo, 0, len(lista_ordenada) - 1)

print(f"\n--- Búsqueda Recursiva ---")
if indice != -1:
    print(f"El número {objetivo} está en el índice {indice}")
else:
    print(f"El número {objetivo} no se encuentra en la lista")