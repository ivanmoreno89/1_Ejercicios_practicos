# Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla si es mayor de edad o no.

""" Mayor de edad

Entradas:
edad (int): edad ingresada por el usuario

Salidas:
(str): print validando si es mayor o menor de edad """

edad = int(input("Digite su edad: "))
if edad > 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
