class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_inicio(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            # Enlazamos el nuevo nodo antes de la cabeza actual
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def eliminar_pista(self, objetivo):
        actual = self.cabeza
        while actual is not None and actual.dato != objetivo:
            actual = actual.siguiente

        if actual is None:
            return False

        # Si el nodo a borrar tiene uno anterior, puenteamos hacia el siguiente
        if actual.anterior is not None:
            actual.anterior.siguiente = actual.siguiente
        else:
            self.cabeza = actual.siguiente

        # Si el nodo a borrar tiene uno siguiente, puenteamos hacia el anterior
        if actual.siguiente is not None:
            actual.siguiente.anterior = actual.anterior
        else:
            self.cola = actual.anterior

        return True

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

# Pruebas del Ejercicio 2
print("Reproductor de Musica")
playlist = ListaDoblementeEnlazada()

playlist.insertar_inicio("Cancion 5")
playlist.insertar_inicio("Cancion 4")
playlist.insertar_inicio("Cancion 3")
playlist.insertar_inicio("Cancion 2")
playlist.insertar_inicio("Cancion 1")

print("Playlist original:")
playlist.recorrer_adelante()

print("\nBorrando Cancion 3...")
playlist.eliminar_pista("Cancion 3")

print("\nPlaylist hacia adelante:")
playlist.recorrer_adelante()

print("\nPlaylist hacia atras:")
playlist.recorrer_atras()