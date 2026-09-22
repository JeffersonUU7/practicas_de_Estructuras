# 1. MAPEO DE REGISTROS
inventario_sku = {
    "SKU-001": {"nombre": "Laptop Dell", "precio": 850.00, "existencia": 12},
    "SKU-002": {"nombre": "Monitor LG 24 pulgadas", "precio": 150.00, "existencia": 8},
    "SKU-003": {"nombre": "Teclado Mecánico", "precio": 45.50, "existencia": 25}
}

print("Resultados de Mapeo de Registros:")
sku_buscar = "SKU-002"
if sku_buscar in inventario_sku:
    producto = inventario_sku[sku_buscar]
    print(f"Encontrado {sku_buscar}: {producto['nombre']} | Precio: ${producto['precio']} | Stock: {producto['existencia']}")

sku_inexistente = "SKU-999"
print(f"Búsqueda segura de {sku_inexistente}:", inventario_sku.get(sku_inexistente, "El producto no existe en el inventario."))
print("\n")


# 2. CONTADOR DE OCURRENCIAS
registro_eventos = [
    "login_exitoso", "error_password", "login_exitoso", 
    "compra_realizada", "error_password", "error_password", 
    "login_exitoso", "cierre_sesion"
]

frecuencia_eventos = {}

for evento in registro_eventos:
    frecuencia_eventos[evento] = frecuencia_eventos.get(evento, 0) + 1

print("Resultados de Contador de Ocurrencias:")
for evento, cantidad in frecuencia_eventos.items():
    print(f"Evento: {evento:<18} | Frecuencia: {cantidad}")
print("\n")


# 3. AGRUPAMIENTO POR CATEGORÍA
lista_elementos = [
    ("Manzana", "Frutas"),
    ("Zanahoria", "Verduras"),
    ("Banana", "Frutas"),
    ("Espinaca", "Verduras"),
    ("Pollo", "Carnes"),
    ("Res", "Carnes")
]

elementos_agrupados = {}

for nombre, categoria in lista_elementos:
    if categoria not in elementos_agrupados:
        elementos_agrupados[categoria] = []
    
    elementos_agrupados[categoria].append(nombre)

print("Resultados de Agrupamiento por Categoría:")
for categoria, elementos in elementos_agrupados.items():
    print(f"Categoría: {categoria}")
    print(f"  -> Elementos: {elementos}")