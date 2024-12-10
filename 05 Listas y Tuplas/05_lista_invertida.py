# Escribir un programa que almacene en una lista los
# números del 1 al 10 y los muestre por pantalla en
# orden inverso separados por comas.


""" Lista invertida

Entradas:
numeros (list): lista de valores

Salidas:
(str): Print con lista invertida """

numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

numeros_invertidos = reversed(numeros)
for n in numeros_invertidos:
    print(n, end=", ")