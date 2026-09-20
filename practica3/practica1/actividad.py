class Edad:
    def __init__(self, valor):
        # La edad no puede ser negativa ni mayor a 120 años.
        if not isinstance(valor, int) or valor < 0 or valor > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")
        self.valor = valor

    def __str__(self):
        return str(self.valor)


class Nota:
    def __init__(self, valor):
        # La nota solamente puede estar entre 0 y 10.
        if not isinstance(valor, (int, float)) or valor < 0 or valor > 10:
            raise ValueError("La nota debe estar entre 0 y 10.")
        self.valor = valor

    def __str__(self):
        return str(self.valor)


class Usuario:
    def __init__(self, nombre):
        # El nombre debe tener al menos 3 caracteres.
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class CodigoCurso:
    def __init__(self, codigo):
        # El código debe comenzar con las letras "CUR" y tener 6 caracteres.
        if not isinstance(codigo, str) or not codigo.startswith("CUR") or len(codigo) != 6:
            raise ValueError("El código debe comenzar con CUR y tener 6 caracteres.")
        self.codigo = codigo

    def __str__(self):
        return self.codigo


class Precio:
    def __init__(self, valor):
        # Un precio no puede ser negativo.
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.valor = valor

    def __str__(self):
        return f"${self.valor:.2f}"


# ---------------------------------------------------------
# EJEMPLOS DE USO
# ---------------------------------------------------------

# 1. EDAD
try:
    edad1 = Edad(20)
    print("Edad válida:", edad1)

    edad2 = Edad(-5)
    print("Edad válida:", edad2)

except ValueError as error:
    print("Edad inválida:", error)


# 2. NOTA
try:
    nota1 = Nota(8.5)
    print("Nota válida:", nota1)

    nota2 = Nota(12)
    print("Nota válida:", nota2)

except ValueError as error:
    print("Nota inválida:", error)


# 3. USUARIO
try:
    usuario1 = Usuario("Jefferson")
    print("Usuario válido:", usuario1)

    usuario2 = Usuario("AB")
    print("Usuario válido:", usuario2)

except ValueError as error:
    print("Usuario inválido:", error)


# 4. CÓDIGO DE CURSO
try:
    curso1 = CodigoCurso("CUR123")
    print("Código de curso válido:", curso1)

    curso2 = CodigoCurso("ABC123")
    print("Código de curso válido:", curso2)

except ValueError as error:
    print("Código de curso inválido:", error)


# 5. PRECIO
try:
    precio1 = Precio(25.50)
    print("Precio válido:", precio1)

    precio2 = Precio(-10)
    print("Precio válido:", precio2)

except ValueError as error:
    print("Precio inválido:", error)