asistencia = [
    [1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

# 1. Mostrar la matriz de asistencia
print("--- Matriz de Asistencia ---")
for fila in asistencia:
    print(fila)

# 2. Asistencias por cada estudiante (recorrido por filas)
print("\n--- Asistencias por Estudiante ---")
totales_por_estudiante = [] # Guardaremos los totales para el paso 4

for i in range(len(asistencia)):
    total_asistencias = 0
    for j in range(len(asistencia[i])):
        if asistencia[i][j] == 1:
            total_asistencias += 1
    totales_por_estudiante.append(total_asistencias)
    print(f"Estudiante {i+1}: {total_asistencias} asistencias")

# 3. Estudiantes que asistieron cada día (recorrido por columnas)
print("\n--- Asistencias por Día ---")
filas_asis = len(asistencia)
col_asis = len(asistencia[0])

for j in range(col_asis):
    asistencias_dia = 0
    for i in range(filas_asis):
        if asistencia[i][j] == 1:
            asistencias_dia += 1
    print(f"Día {j+1}: {asistencias_dia} estudiantes asistieron")

# 4. Identificar al estudiante con mayor cantidad de asistencias
print("\n--- Estudiante con Más Asistencias ---")
max_asistencias = totales_por_estudiante[0]

# Encontrar el valor máximo
for total in totales_por_estudiante:
    if total > max_asistencias:
        max_asistencias = total

# Mostrar los estudiantes que tengan ese valor máximo (puede haber empates)
for i in range(len(totales_por_estudiante)):
    if totales_por_estudiante[i] == max_asistencias:
        print(f"El Estudiante {i+1} tiene la mayor cantidad con {max_asistencias} asistencias.")