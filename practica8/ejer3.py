class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        
        
print("--- EJERCICIO 3: AUDITORÍA DE CARPETAS ---")

# Estructura del árbol (Carpetas y archivos)
disco_c = Nodo("Carpeta_Principal")

disco_c.izq = Nodo("Carpeta_Documentos")
disco_c.der = Nodo("Carpeta_Imagenes")

# Archivos finales en Documentos
disco_c.izq.izq = Nodo("tarea_estructuras.pdf")
disco_c.izq.der = Nodo("apuntes.docx")

# Archivos finales en Imagenes
disco_c.der.izq = Nodo("foto_perfil.png")
disco_c.der.der = Nodo("meme_gato.jpg")

# 1. Función para contar TODOS los nodos (del ejemplo)
def contar_nodos(nodo):
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.izq) + contar_nodos(nodo.der)

# 2. Función NUEVA: Contar solo hojas (archivos finales)
def contar_hojas(nodo):
    if nodo is None:
        return 0
    # Si no tiene hijo izquierdo ni derecho, es una hoja
    if nodo.izq is None and nodo.der is None:
        return 1
    # Si no es hoja, seguimos buscando hacia abajo
    return contar_hojas(nodo.izq) + contar_hojas(nodo.der)

# 3. Función de búsqueda (del ejemplo)
def buscar_valor(nodo, objetivo):
    if nodo is None:
        return False
    if nodo.valor.lower() == objetivo.lower(): # Le puse lower() para que no importe si el user usa mayúsculas
        return True
    return buscar_valor(nodo.izq, objetivo) or buscar_valor(nodo.der, objetivo)

# Pruebas del ejercicio
print(f"Total de elementos (Carpetas + Archivos): {contar_nodos(disco_c)}")
print(f"Total de archivos finales (Hojas): {contar_hojas(disco_c)}")

# Interacción con el usuario (como pidió la práctica)
archivo_a_buscar = input("\nIngresa el nombre del archivo que quieres buscar (ej. meme_gato.jpg): ")

if buscar_valor(disco_c, archivo_a_buscar):
    print(f"¡Éxito! El archivo '{archivo_a_buscar}' SÍ se encuentra en el sistema.")
else:
    print(f"Error: El archivo '{archivo_a_buscar}' NO existe.")