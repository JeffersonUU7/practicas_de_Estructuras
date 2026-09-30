inventario = [
    [15, 12, 10],
    [8, 10, 7],
    [20, 18, 15],
    [12, 14, 11]
]

# 1. Mostrar la matriz de inventario
print("--- Matriz de Inventario ---")
for fila in inventario:
    print(fila)

# 2. Calcular el total disponible de cada producto (recorrido por filas)
print("\n--- Total por Producto ---")
for i in range(len(inventario)):
    total_producto = 0
    for j in range(len(inventario[i])):
        total_producto += inventario[i][j]
    print(f"Producto {i+1}: {total_producto}")

# 3. Calcular el total registrado en cada día (recorrido por columnas)
print("\n--- Total por Día ---")
filas = len(inventario)
columnas = len(inventario[0])

for j in range(columnas):
    total_dia = 0
    for i in range(filas):
        total_dia += inventario[i][j]
    print(f"Día {j+1}: {total_dia}")

# 4. Modificar la cantidad de un producto
print("\n--- Modificar Inventario ---")
# Se resta 1 porque los índices en Python comienzan en 0
fila_mod = int(input("Ingrese el número de producto (1 a 4): ")) - 1
col_mod = int(input("Ingrese el día (1 a 3): ")) - 1
nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

if 0 <= fila_mod < filas and 0 <= col_mod < columnas:
    inventario[fila_mod][col_mod] = nueva_cantidad
    print("\nInventario actualizado:")
    for fila in inventario:
        print(fila)
else:
    print("Las posiciones ingresadas no son válidas.")