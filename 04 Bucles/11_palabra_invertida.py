# Escribir un programa que pida al usuario una palabra
# y luego muestre por pantalla una a una las letras de
# la palabra introducida empezando por la última.


""" Palabra invertida

Entradas:
palabra (str): Palabra ingresada por el usuario
palabra_invertida (str): palabra inversida

Salidas:
(str): print de la palabra invertida letra por letra """

palabra = input("Introduzca una palabra:\n")
palabra_invertida = reversed(palabra)
for n in palabra_invertida:
    print(n, sep="\n")