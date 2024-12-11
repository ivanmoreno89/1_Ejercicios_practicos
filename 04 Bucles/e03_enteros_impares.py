# Escribir un programa que pida al usuario un número
# entero positivo y muestre por pantalla todos los
# números impares desde 1 hasta ese número separados
# por comas.

""" Imprimir números impares hasta el número ingresado

Entradas:
entero (int): Número ingresado por el usuario
n (int): contador

Salidas:
(int): enteros impares separados por comas """

entero = int(input("Escriba un número entero positivo:\n"))
for n in range(1,entero+1, 2):
    print(n, end=", ")
