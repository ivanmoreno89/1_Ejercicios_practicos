# Escribir un programa que pida al usuario un número
# entero y muestre por pantalla un triángulo rectángulo
# como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

""" Imprimir un triangulo de lado n introducido por el usuario

Entradas:
lado (int): Valor del lado ingresado por el usuario
n (int): Contador

Salidas:
(str): Triangulo de altura n ingresada por el usuario """

lado=int(input("Ingrese un numero entero, el cual será el lado del triangulo:\n"))

for n in range(lado+1):
    print("*"*n)
