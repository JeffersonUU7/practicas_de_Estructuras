def maximo_recursivo(lista):
    # Caso base: si solo queda un elemento, lógicamente ese es el mayor
    if len(lista) == 1:
        return lista[0]
    
    # Caso recursivo: guardamos el primer elemento y evaluamos el resto de la lista
    cabeza = lista[0]
    max_del_resto = maximo_recursivo(lista[1:])
    
    # Comparamos para ver quién "gana" y sube en la pila de ejecución
    if cabeza > max_del_resto:
        return cabeza
    else:
        return max_del_resto

# Prueba
print(f"El máximo de [3, 18, 2, 45, 9] es: {maximo_recursivo([3, 18, 2, 45, 9])}")