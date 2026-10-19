class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        
        # si la lista esta vacia, el nuevo nodo es el primero
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        # si no, avanzamos hasta encontrar el ultimo nodo
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        
        # lo conectamos al final
        actual.siguiente = nuevo_nodo

    def recorrer(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# pruebas del ejercicio 1
historial = ListaEnlazada()
historial.insertar_final("google.com")
historial.insertar_final("youtube.com")
historial.insertar_final("github.com")
historial.insertar_final("stackoverflow.com")

print("Historial de navegacion:")
historial.recorrer()