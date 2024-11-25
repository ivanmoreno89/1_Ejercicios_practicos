# Escribir un programa que pregunte al usuario su
# edad y muestre por pantalla todos los años que
# ha cumplido (desde 1 hasta su edad).

""" Ingresando la edad, imprimir mensaje por cada año cumplido

Entradas:
edad (int): Edad del usuario
n (int): contador

Salidas:
(str): Mensaje con años cumplidos de acuerdo a la cantidad de años """

edad = int(input("Cuántos años tiene ud?: "))
for n in range(edad):
    print(f"has cumplido {n+1} años")
