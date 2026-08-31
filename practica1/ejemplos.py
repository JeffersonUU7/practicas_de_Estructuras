class Edad:
    def __init__(self, valor):
        if not isinstance(valor, int) or valor < 0 or valor > 120:
            raise ValueError("Edad uera del rango permitido (0 y 120)")
        self.valor = valor

class Nota:
    def __init__(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0 or valor > 10:
            raise ValueError("La nota debe estar entre 0 y 10.")
        self.valor = valor

    def __str__(self):
        return str(self.valor)

try:
    edad1 = Edad(20)
    edad2 = Edad(-5)
    nota1 = Nota(8.5)
    nota2 = Nota(15)
except ValueError as e:
    print("Nota invalida:", e)