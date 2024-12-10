# Escribir un programa que pida al usuario un
# número entero y muestre por pantalla si es
# un número primo o no.


""" número primo

Entradas:
numero (int): número ingresado por el usuario
i (int): valor del residuo para el iterador

Salidas:
(str): print indicando si el número es primo o no """

numero = int(input("Escriba un número entero:\n"))
i = 2
while numero % i != 0:
    i += 1

if i == numero:
    print("es primo")
else:
    print("no es primo")
