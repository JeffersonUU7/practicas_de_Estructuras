class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        
print("--- EJERCICIO 1: ÁRBOL GENEALÓGICO ---")

# Nivel 1: Raíz (Abuelos)
raiz_familia = Nodo("Abuela Santana")

# Nivel 2: Hijos (Tíos/Padres)
raiz_familia.izq = Nodo("Tía Roxy")
raiz_familia.der = Nodo("Papá Alexx")

# Nivel 3: Nietos (Descendientes)
# Hijos de la Tía Carmen
raiz_familia.izq.izq = Nodo("Primo Cristian")
raiz_familia.izq.der = Nodo("Prima Melissa")

# Hijos de Papá José
raiz_familia.der.izq = Nodo("Yo (Jefferson)")
raiz_familia.der.der = Nodo("Hermana Kitssia")

# Imprimiendo para comprobar (como pidió el profe, a mano)
print(f"Raíz (Abuela): {raiz_familia.valor}")
print(f"Hijos de {raiz_familia.valor}: {raiz_familia.izq.valor} y {raiz_familia.der.valor}")
print(f"Hijos de {raiz_familia.izq.valor}: {raiz_familia.izq.izq.valor} y {raiz_familia.izq.der.valor}")
print(f"Hijos de {raiz_familia.der.valor}: {raiz_familia.der.izq.valor} y {raiz_familia.der.der.valor}\n")