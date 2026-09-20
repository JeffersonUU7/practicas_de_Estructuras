# Actividad de Estructuras de Datos
# Uso de listas, tuplas y set


# 1. Lista de reproducción musical


# Una lista sirve porque podemos agregar,
# eliminar o cambiar canciones cuando queramos.
canciones = ["Perfect", "Believer", "Shape of You", "Faded"]

print("Lista de reproducción:")
for cancion in canciones:
    print("-", cancion)

# Agregamos otra canción a la lista
canciones.append("Counting Stars")

print("\nDespués de agregar una canción:")
print(canciones)


# 2. Colección de videojuegos


# La tupla se utiliza cuando queremos guardar
# datos que no necesitamos modificar.
videojuegos = ("Minecraft", "FIFA 25", "GTA V", "Forza Horizon")

print("\nColección de videojuegos:")
for juego in videojuegos:
    print("-", juego)



# 3. Registro de cursos aprobados


# El set evita que se repitan los cursos.
# Esto es útil si por error agregamos el mismo curso.
cursos_aprobados = {"Programación", "Matemática", "Inglés"}

# Intentamos agregar un curso que ya existe
cursos_aprobados.add("Programación")

print("\nCursos aprobados:")
for curso in cursos_aprobados:
    print("-", curso)


# 4. Participantes de un evento


# Una lista permite llevar el registro de los
# participantes y también agregar nuevos nombres.
participantes = ["Carlos", "Ana", "Luis", "María"]

print("\nParticipantes del evento:")
for participante in participantes:
    print("-", participante)

# Se agrega un nuevo participante
participantes.append("José")

print("\nParticipantes actualizados:")
print(participantes)



# 5. Inventario básico de productos

# Un set es útil porque no permite que un mismo
# producto aparezca repetido.
productos = {"Laptop", "Mouse", "Teclado", "Audífonos"}

# Agregamos un producto nuevo
productos.add("Monitor")

print("\nInventario de productos:")
for producto in productos:
    print("-", producto)



# Justificación de los tipos de datos


print("\n--- Justificación ---")

print("""
Lista:
Se utiliza para la reproducción musical y los participantes
porque son datos que pueden cambiar, agregar o eliminar elementos.

Tupla:
Se utiliza para los videojuegos porque en este ejemplo
solo necesitamos guardar los datos y no modificarlos.

Set:
Se utiliza para los cursos aprobados y el inventario porque
evita que existan elementos repetidos.
""")