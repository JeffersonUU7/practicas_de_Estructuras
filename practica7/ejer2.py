temperaturas = [
    [24, 28, 25],
    [23, 29, 26],
    [25, 30, 27],
    [22, 27, 24],
    [24, 28, 26]
]

# 1. Mostrar la matriz de temperaturas
print("--- Matriz de Temperaturas ---")
for fila in temperaturas:
    print(fila)

# 2. Promedio de temperatura de cada día (recorrido por filas)
print("\n--- Promedio por Día ---")
for i in range(len(temperaturas)):
    total_dia = 0
    for j in range(len(temperaturas[i])):
        total_dia += temperaturas[i][j]
    promedio_dia = total_dia / len(temperaturas[i])
    print(f"Día {i+1}: {promedio_dia:.2f}°")

# 3. Promedio correspondiente a cada momento del día (recorrido por columnas)
print("\n--- Promedio por Momento del Día ---")
filas_temp = len(temperaturas)
col_temp = len(temperaturas[0])

for j in range(col_temp):
    total_momento = 0
    for i in range(filas_temp):
        total_momento += temperaturas[i][j]
    promedio_momento = total_momento / filas_temp
    print(f"Momento {j+1}: {promedio_momento:.2f}°")

# 4. Determinar la temperatura más alta registrada
print("\n--- Temperatura Máxima ---")
temp_maxima = temperaturas[0][0]

for fila in temperaturas:
    for valor in fila:
        if valor > temp_maxima:
            temp_maxima = valor

print(f"La temperatura más alta registrada es: {temp_maxima}°")