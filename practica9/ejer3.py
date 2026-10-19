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

    def contar_elementos(self):
        # sumamos 1 por cada nodo por el que pasamos
        total = 0
        actual = self.cabeza
        while actual is not None:
            total += 1
            actual = actual.siguiente
        return total

    def obtener_posicion(self, indice):
        actual = self.cabeza
        posicion = 0
        
        while actual is not None:
            # si encontramos el indice devolvemos el dato
            if posicion == indice:
                return actual.dato
            posicion += 1
            actual = actual.siguiente
            
        # si termina el bucle y no lo encontro, se salio del limite
        return "El indice excede el tamano"

    def recorrer(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# pruebas del ejercicio 3
memoria = ListaEnlazada()
memoria.insertar_final("Nodo A")
memoria.insertar_final("Nodo B")
memoria.insertar_final("Nodo C")
memoria.insertar_final("Nodo D")
memoria.insertar_final("Nodo E")

print("Estructura en memoria:")
memoria.recorrer()

print(f"\nCantidad total de nodos: {memoria.contar_elementos()}")
print(f"Dato en el indice 2: {memoria.obtener_posicion(2)}")
print(f"Dato en el indice 10: {memoria.obtener_posicion(10)}")