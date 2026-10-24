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

    def buscar_desde_cabeza(self, objetivo):
        actual = self.cabeza
        iteraciones = 0
        while actual is not None:
            iteraciones += 1
            if actual.dato == objetivo:
                return iteraciones
            actual = actual.siguiente
        return iteraciones

    def buscar_desde_cola(self, objetivo):
        actual = self.cola
        iteraciones = 0
        # Recorremos con el puntero anterior para buscar en reversa
        while actual is not None:
            iteraciones += 1
            if actual.dato == objetivo:
                return iteraciones
            actual = actual.anterior
        return iteraciones

# Pruebas del Ejercicio 3
print("Busqueda Bidireccional Optima")
datos = ListaDoblementeEnlazada()

for letra in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
    datos.insertar_final(letra)
    
objetivo = 'I'
print(f"Buscando el elemento {objetivo}")

iter_cabeza = datos.buscar_desde_cabeza(objetivo)
print(f"Iteraciones buscando desde la cabeza: {iter_cabeza}")

iter_cola = datos.buscar_desde_cola(objetivo)
print(f"Iteraciones buscando desde la cola: {iter_cola}")