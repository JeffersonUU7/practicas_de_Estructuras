import time
import random

# Reutilizamos el algoritmo de Burbuja clásico
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Reutilizamos el QuickSort con pivote central
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    return quicksort(menores) + iguales + quicksort(mayores)

# Generamos 10,000 números aleatorios entre 1 y 50,000
datos_aleatorios = [random.randint(1, 50000) for _ in range(10000)]

# Creamos copias independientes para que ambos ordenen el mismo desorden
copia_burbuja = datos_aleatorios.copy()
copia_quicksort = datos_aleatorios.copy()

print("Iniciando pruebas de rendimiento con 10,000 elementos...\n")

# Prueba Burbuja O(n^2)
inicio_b = time.time()
burbuja(copia_burbuja)
fin_b = time.time()
tiempo_burbuja = fin_b - inicio_b
print(f"Tiempo Burbuja: {tiempo_burbuja:.4f} segundos")

# Prueba QuickSort O(n log n)
inicio_q = time.time()
quicksort(copia_quicksort)
fin_q = time.time()
tiempo_quicksort = fin_q - inicio_q
print(f"Tiempo QuickSort: {tiempo_quicksort:.4f} segundos")