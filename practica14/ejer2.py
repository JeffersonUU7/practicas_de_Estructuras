def seleccion_descendente(calificaciones):
    n = len(calificaciones)
    
    for i in range(n):
        # Ahora asumimos que el actual es el mayor, no el menor
        max_idx = i
        
        for j in range(i + 1, n):
            # Cambio clave: evaluamos si el elemento en j es MAYOR que nuestro máximo actual
            if calificaciones[j] > calificaciones[max_idx]:
                max_idx = j
                
        # Intercambiamos la posición actual con la del número más grande que encontramos
        calificaciones[i], calificaciones[max_idx] = calificaciones[max_idx], calificaciones[i]
        
    return calificaciones

# Prueba
notas = [7.5, 9.0, 6.2, 10.0, 5.5, 8.8]
print(f"Calificaciones originales: {notas}")
print(f"Calificaciones de mayor a menor: {seleccion_descendente(notas)}")