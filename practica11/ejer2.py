def contar_digitos(n):
    # Asegurarnos de trabajar con el valor absoluto por si ingresan negativos
    n = abs(n)
    
    # Caso base: si el número es menor a 10, es de un solo dígito
    if n < 10:
        return 1
    
    # Caso recursivo: sumamos 1 (por el dígito que quitamos) 
    # y pasamos el número sin ese último dígito (n // 10)
    return 1 + contar_digitos(n // 10)

# Prueba
print(f"Dígitos de 4528: {contar_digitos(4528)}")
print(f"Dígitos de 9: {contar_digitos(9)}")