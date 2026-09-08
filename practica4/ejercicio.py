from collections import deque

print("Control de biblioteca y centro de computo\n")

# Sistema FIFO
print("1. Fila para usar las computadoras")

# fila vacia
fila_compus = deque()

# Van llegando los chavos
fila_compus.append("Mateo")
fila_compus.append("Luis")
fila_compus.append("Andrea")

print(f"Alumnos esperando: {list(fila_compus)}")

# Asignando compus en orden de llegada
if len(fila_compus) > 0:
    alumno = fila_compus.popleft()
    print(f"Pasando a maquina a: {alumno}")

if len(fila_compus) > 0:
    alumno = fila_compus.popleft()
    print(f"Pasando a maquina a: {alumno}")

if len(fila_compus) > 0:
    alumno = fila_compus.popleft()
    print(f"Pasando a maquina a: {alumno}")

print(f"Fila despues de asignar: {list(fila_compus)}")

# Tratar de asignar si no hay nadie
if len(fila_compus) > 0:
    alumno = fila_compus.popleft()
    print(f"Pasando a maquina a: {alumno}")
else:
    print("Aviso: Ya no hay alumnos esperando equipo")


# Sistema LIFO
print("\n2. Devolucion de libros")

# caja donde se apilan los libros
caja_libros = []

# Se van apilando
caja_libros.append("Redes de Computadoras")
caja_libros.append("Programacion en C")
caja_libros.append("Base de datos")

print(f"Libros en la caja: {caja_libros}")

# El bibliotecario saca el que quedo arriba de la pila
while len(caja_libros) > 0:
    libro = caja_libros.pop()
    print(f"Registrando libro devuelto: {libro}")

# Sacar cuando la caja ya esta vacia
if len(caja_libros) > 0:
    libro = caja_libros.pop()
    variable_basura = 0 # solo para rellenar
    print(f"Registrando: {libro}")
else:
    print("Error: No se puede sacar nada porque la caja esta vacia")


# sets
print("\n3. Accesos y prestamos")

# carnets permitidos
carnets_validos = {
    "SM202401",
    "SM202402",
    "SM202403"
}

libros_prestados = set()

# Chequear si el carnet existe
mi_carnet = "SM202401"

if mi_carnet in carnets_validos:
    print(f"El carnet {mi_carnet} es valido para prestamos. Pase.")
else:
    print(f"Carnet {mi_carnet} denegado")


# Prestar un libro a un alumno
codigo_libro = "LIB-001"

if codigo_libro in libros_prestados:
    print(f"Error: El libro {codigo_libro} ya lo tiene alguien mas")
else:
    libros_prestados.add(codigo_libro)
    print(f"Prestamo del libro {codigo_libro} guardado en el sistema")


# Intentar prestar el mismo otra vez por error
codigo_repetido = "LIB-001"

if codigo_repetido in libros_prestados:
    print(f"Error: El libro {codigo_libro} ya esta prestado, elige otro")
else:
    libros_prestados.add(codigo_repetido)
    print(f"Prestamo del libro {codigo_libro} exitoso")


print("\n ESTADO FINAL DE LAS VARIABLES")
print(f"Fila de compus: {list(fila_compus)}")
print(f"Caja de libros: {caja_libros}")
print(f"Carnets del sistema: {carnets_validos}")
print(f"Libros ocupados: {libros_prestados}")