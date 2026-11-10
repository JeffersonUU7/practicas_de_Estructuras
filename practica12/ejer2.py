class NodoImagen:
    def __init__(self, archivo):
        self.archivo = archivo
        self.siguiente = None
        self.anterior = None

class CarruselInfinito:
    def __init__(self):
        self.cabeza = None
        self.actual = None # Puntero de navegación en tiempo real

    def agregar_imagen(self, archivo):
        nueva = NodoImagen(archivo)
        if not self.cabeza:
            self.cabeza = nueva
            # Siendo el único elemento, es su propio anterior y siguiente
            nueva.siguiente = nueva
            nueva.anterior = nueva
            self.actual = nueva 
        else:
            cola = self.cabeza.anterior
            cola.siguiente = nueva
            nueva.anterior = cola
            nueva.siguiente = self.cabeza
            self.cabeza.anterior = nueva

    def ver_actual(self):
        if self.actual:
            print(f"Mostrando en pantalla: [{self.actual.archivo}]")

    def avanzar(self):
        if self.actual:
            print(">> Siguiente imagen...")
            self.actual = self.actual.siguiente
            self.ver_actual()

    def retroceder(self):
        if self.actual:
            print("<< Imagen anterior...")
            self.actual = self.actual.anterior
            self.ver_actual()


# Prueba
galeria = CarruselInfinito()
galeria.agregar_imagen("foto_vacaciones.jpg")
galeria.agregar_imagen("diagrama_bd.png")
galeria.agregar_imagen("mascota.jpeg")
galeria.agregar_imagen("captura_pantalla.png")

print("--- Estado Inicial ---")
galeria.ver_actual()

print("\n--- Avanzando ---")
galeria.avanzar()
galeria.avanzar()
galeria.avanzar()
galeria.avanzar() # Aquí ocurre la magia circular: vuelve a foto_vacaciones.jpg

print("\n--- Retrocediendo ---")
galeria.retroceder() # Y aquí vuelve a la captura de pantalla sin errores