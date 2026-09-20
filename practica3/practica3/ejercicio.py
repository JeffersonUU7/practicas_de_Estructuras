"""
Ejercicios Prácticos de Estructuras de Datos
Aplicación de patrones LIFO y Álgebra de Sets
"""


# CASO 1: LIFO (Last In First Out) - Pila
# Sistema de navegación en un navegador web


print("=" * 60)
print("CASO 1: LIFO - Historial de Navegación Web")
print("=" * 60)

pila_navegacion = []

# Simular navegación a diferentes páginas
paginas = ["google.com", "github.com", "stackoverflow.com", "youtube.com"]

print("\nNavigando a las siguientes páginas:")
for pagina in paginas:
    pila_navegacion.append(pagina)
    print(f"  → Visitando: {pagina}")

print(f"\nHistorial de navegación: {pila_navegacion}")

# Simular botón atrás
print("\n--- Presionando botón ATRÁS ---")
ultima_pagina = pila_navegacion.pop()
print(f"Saliendo de: {ultima_pagina}")
print(f"Página actual: {pila_navegacion[-1]}")

print(f"\nHistorial actualizado: {pila_navegacion}")

# CASO 2: Álgebra de Sets - Conjunto
# Sistema de filtrado de permisos de usuario


print("\n" + "=" * 60)
print("CASO 2: Sets - Validación de Permisos de Acceso")
print("=" * 60)

# Permisos solicitados por un usuario (pueden tener duplicados)
permisos_solicitados = [
    "lectura", "escritura", "lectura", "eliminacion", 
    "escritura", "admin", "lectura", "admin"
]

print(f"\nPermisos solicitados (con duplicados): {permisos_solicitados}")

# Convertir a conjunto para eliminar duplicados
permisos_unicos = set(permisos_solicitados)
print(f"Permisos únicos permitidos: {permisos_unicos}")

# Calcular estadísticas
permisos_duplicados = len(permisos_solicitados) - len(permisos_unicos)
print(f"Permisos duplicados removidos: {permisos_duplicados}")

# Operaciones con sets
print("\n--- Operaciones adicionales con Sets ---")

# Permisos disponibles en el sistema
permisos_sistema = {"lectura", "escritura", "eliminacion", "admin", "backup"}
print(f"Permisos disponibles en el sistema: {permisos_sistema}")

# Permisos válidos (intersección)
permisos_validos = permisos_unicos & permisos_sistema
print(f"Permisos válidos otorgados: {permisos_validos}")

# Permisos solicitados pero no disponibles
permisos_negados = permisos_unicos - permisos_sistema
print(f"Permisos solicitados no disponibles: {permisos_negados}")

# Permisos disponibles pero no solicitados
permisos_sin_solicitar = permisos_sistema - permisos_unicos
print(f"Permisos no solicitados: {permisos_sin_solicitar}")

print("\n" + "=" * 60)
print("Ejercicio completado exitosamente")
print("=" * 60)
