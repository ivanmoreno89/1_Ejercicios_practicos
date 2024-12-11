# Escribir un programa que almacene en una lista los
# siguientes precios, 50, 75, 46, 22, 80, 65, 8, y
# muestre por pantalla el menor y el mayor de los precios.

""" Precio mínimo y máximo

Entradas:
preios (list): Lista de precios
minimo (int): Precio mínimo de la lista
maximo (int): Precio máximo de la lista

Salidas:
(str): Print con información del precio mínimo y el máximo """

# Variables de entrada
precios = [50, 75, 46, 22, 80, 65, 8]
print(min(precios))
print(max(precios))

precios.sort()
minimo = maximo = precios[0]
print(precios)

for precio in precios:
    if precio < minimo:
        minimo = precio
    elif precio > maximo:
        maximo = precio

print(f"El mínimo es {minimo}")
print(f"El máximo es {maximo}")
