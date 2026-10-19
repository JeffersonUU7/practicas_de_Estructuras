class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_inicio(self):
        # si no hay nada en la lista, no hacemos nada
        if self.cabeza is None:
            return None
        
        # guardamos el valor antes de mover la cabeza para no perderlo
        dato_procesado = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        
        return dato_procesado

    def recorrer(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# pruebas del ejercicio 2
tareas = ListaEnlazada()
tareas.insertar_final("Actualizar sistema")
tareas.insertar_final("Hacer backup")
tareas.insertar_final("Reiniciar servidor")

print("Tareas pendientes:")
tareas.recorrer()

# despachamos las tareas una por una hasta que quede vacia
while tareas.cabeza is not None:
    tarea = tareas.eliminar_inicio()
    print(f"\nProcesando: {tarea}")
    print("Tareas restantes:")
    tareas.recorrer()
    