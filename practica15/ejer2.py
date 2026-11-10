import sys
import time
# Aumentamos el límite de recursividad de Python por seguridad en esta prueba
sys.setrecursionlimit(2000)

def quicksort_primer_pivote(lista):
    if len(lista) <= 1:
        return lista
    
    # Modificación: Siempre tomamos el primer elemento como pivote
    pivote = lista[0]
    
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    return quicksort_primer_pivote(menores) + iguales + quicksort_primer_pivote(mayores)

# Prueba con una lista que YA está ordenada
lista_ordenada = list(range(1, 1001)) # Del 1 al 1000

inicio = time.time()
quicksort_primer_pivote(lista_ordenada)
fin = time.time()

print(f"Tiempo QuickSort (Primer pivote / Lista ordenada): {fin - inicio:.4f} segundos")