# Tipos primitivos
x = 10
print(x, id(x))

x = x + 1
print(x, id(x))

texto = "hola"
print(texto, id(texto))

texto = texto + " mundo"
print(texto, id(texto))


lista = [1, 2, 3]
print(lista, id(lista))

lista.append(4)
print(lista, id(lista))

# tulpa = (1, 2, 3)
# try:
#     tulpa[0] = 99
# except TypeError as e:
#     print(e)


# paso por valor vs paso porr referencia
def modificar_numero(num):
    num += 10
    print("dentro de funcion", num)


val = 5
modificar_numero(val)
print("fuera de la funcion", val)


def modificar_lista(lst):
    lst.append(99)


mi_lista = [1, 2]
modificar_lista(mi_lista)
print("lista modificada ", mi_lista)