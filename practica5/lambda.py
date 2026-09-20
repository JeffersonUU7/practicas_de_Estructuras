"""
Práctica: Funciones Anónimas (Lambda) en Python
Manejo y Estructura de Datos
"""


# 1. REFACTORIZACIÓN DE FUNCIONES CONVENCIONALES

print("- 1. REFACTORIZACIÓN DE FUNCIONES -")

# A. Cálculo de descuentos
calcular_descuento = lambda precio, descuento: precio - (precio * descuento)
print(f"Precio original: $100, Descuento: 20% -> Precio con descuento: ${calcular_descuento(100, 0.20)}")

# B. Conversión de temperatura (Celsius a Fahrenheit)
convertir_temperatura = lambda celsius: (celsius * 9/5) + 32
print(f"30°C equivalen a -> {convertir_temperatura(30)}°F")

# C. Formateo de nombres (Ej: REQUENO, Jefferson)
formatear_nombre = lambda nombre, apellido: f"{apellido.upper()}, {nombre.capitalize()}"
print(f"Nombres sin formato: 'jefferson requeno' -> Formateado: {formatear_nombre('jefferson', 'requeno')}")


# 2. VALIDACIONES CON OPERADORES TERNARIOS

print("\n- 2. VALIDACIONES CON TERNARIOS -")

# A. Determinar si un número es positivo o negativo
evaluar_signo = lambda n: "Positivo" if n >= 0 else "Negativo"
print(f"Evaluando el número -5: {evaluar_signo(-5)}")
print(f"Evaluando el número 10: {evaluar_signo(10)}")

# B. Determinar si un usuario cumple la mayoría de edad (retorna Booleano)
es_mayor_edad = lambda edad: True if edad >= 18 else False
print(f"¿Usuario de 17 años es mayor de edad?: {es_mayor_edad(17)}")
print(f"¿Usuario de 21 años es mayor de edad?: {es_mayor_edad(21)}")



# 3. PROCESAMIENTO EN LOTE

print("\n- 3. PROCESAMIENTO EN LOTE -")

# Aplicar un recargo del 5% a una lista de precios
precios_base = [15.50, 40.00, 120.00, 8.75]

# Lambda que calcula el recargo y redondea a 2 decimales
aplicar_recargo = lambda p: round(p * 1.05, 2)

# Usamos la comprensión de listas para iterar y aplicar la función lambda
precios_actualizados = [aplicar_recargo(precio) for precio in precios_base]

print(f"Precios originales: {precios_base}")
print(f"Precios con 5% de recargo: {precios_actualizados}")


