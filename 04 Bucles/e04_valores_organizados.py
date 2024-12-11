# Escribir un programa que pida al usuario un número entero
# positivo y muestre por pantalla la cuenta atrás desde ese
# número hasta cero separados por comas.

""" Imprimir números de mayor a menor desde el valor ingresado

Entradas:
entero (int): Número ingresado por el usuario
n (int): contador

Salidas:
(int): Valores de mayor a menor separados por comas """

entero = int(input("Escriba un número entero:\n"))
for n in range(entero,-1, -1):
    print(n, end=", ")
