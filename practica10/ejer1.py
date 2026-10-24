class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def recorrer_adelante(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def recorrer_atras(self):
        actual = self.cola
        while actual is not None:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior
        print("None")

# Pruebas del Ejercicio 1
print("Historial de Navegacion")
historial = ListaDoblementeEnlazada()

historial.insertar_final("google.com")
historial.insertar_final("wikipedia.org")
historial.insertar_final("github.com")
historial.insertar_final("stackoverflow.com")
historial.insertar_final("youtube.com")

print("Avanzando en las paginas:")
historial.recorrer_adelante()

print("\nRetrocediendo en el historial:")
historial.recorrer_atras()