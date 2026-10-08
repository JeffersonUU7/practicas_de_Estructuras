class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        
        
print("--- EJERCICIO 2: SOPORTE TÉCNICO ---")

# Construyendo el árbol de decisiones
soporte = Nodo("¿La PC enciende?")

# Rama Izquierda (Sí enciende)
soporte.izq = Nodo("¿Muestra imagen?")
soporte.izq.izq = Nodo("Revisar sistema operativo (Fin)")
soporte.izq.der = Nodo("Revisar tarjeta de video (Finnnl")

# Rama Derecha (No enciende)
soporte.der = Nodo("¿Está conectada?")
soporte.der.izq = Nodo("Probar otro enchufe (Fin)")
soporte.der.der = Nodo("Cambiar fuente de poder (Fin)")

# Funciones de recorrido del ejemplo
def preorden(nodo):
    if nodo is not None:
        print(f"- {nodo.valor}")
        preorden(nodo.izq)
        preorden(nodo.der)

def postorden(nodo):
    if nodo is not None:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(f"- {nodo.valor}")

print("Recorrido PREORDEN (Orden de evaluación desde la raíz):")
preorden(soporte)

print("\nRecorrido POSTORDEN (Cierre de procesos, de hojas a raíz):")
postorden(soporte)
print()