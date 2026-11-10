def potencia(base, exponente):
    # Caso base: el exponente llega a 0, detenemos las llamadas
    if exponente == 0:
        return 1
    
    # Caso recursivo: multiplicamos la base actual y reducimos el exponente
    return base * potencia(base, exponente - 1)

# Prueba
print(f"2 elevado a la 3 es: {potencia(2, 3)}")
print(f"5 elevado a la 4 es: {potencia(5, 4)}")