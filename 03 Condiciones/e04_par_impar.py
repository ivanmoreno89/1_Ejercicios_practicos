# Escribir un programa que pida al usuario un número
# entero y muestre por pantalla si es par o impar.

""" Par o impar

Entradas:
entero (int): entero ingresado por el usuario

Salidas:
(str): print indicando si el número ingresado es par o impar """

entero = int(input("Ingrese un número entero: "))

if entero%2 == 0:
    print(f"El número {entero} es par")
else:
    print(f"El número {entero} es impar")
