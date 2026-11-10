def busqueda_secuencial_pasos(lista, objetivo):
    iteraciones = 0
    for i in range(len(lista)):
        iteraciones += 1
        if lista[i] == objetivo:
            return (i, iteraciones)
    
    # Si no lo encuentra, también devolvemos cuántos pasos dio
    return (-1, iteraciones)

def busqueda_binaria_pasos(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    iteraciones = 0
    
    while inicio <= fin:
        iteraciones += 1
        medio = (inicio + fin) // 2
        
        if lista[medio] == objetivo:
            return (medio, iteraciones)
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
            
    return (-1, iteraciones)

# Prueba comparativa
# Generamos una lista ordenada del 1 al 1000
datos_1000 = list(range(1, 1001))
numero_a_buscar = 998 

print("--- Comparativa de Rendimiento ---")
resultado_sec, pasos_sec = busqueda_secuencial_pasos(datos_1000, numero_a_buscar)
print(f"Secuencial -> Posición: {resultado_sec}, Iteraciones requeridas: {pasos_sec}")

resultado_bin, pasos_bin = busqueda_binaria_pasos(datos_1000, numero_a_buscar)
print(f"Binaria    -> Posición: {resultado_bin}, Iteraciones requeridas: {pasos_bin}")